import spacy
from spacy.training import Example

from .language import load_model

NER_PIPE = 'ner'


class NERModel(object):
    def __init__(self, language, disable_pipes=False):
        self.nlp = load_model(language)
        self.language = language
        if disable_pipes:
            self.nlp.select_pipes(enable=NER_PIPE)

    @classmethod
    def load(cls, model_path):
        cls.nlp = spacy.load(model_path)
        cls.language = cls.nlp.lang

    def update(self, entities, text):
        annotations = {'entities': entities}
        example = Example.from_dict(self.nlp.make_doc(text), annotations)
        self.nlp.update([example])

    def predict(self, text):
        doc = self.nlp(text)
        entities = []
        for ent in doc.ents:
            entities.append([ent.start, ent.end, ent.label_])
        return entities

    def to_disk(self, path):
        self.nlp.to_disk(path)

    def get_ent_labels(self):
        return self.nlp.get_pipe(NER_PIPE).labels
