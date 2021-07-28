import spacy
from spacy.training import Example

NER_PIPE = 'ner'
MODELS_DICT = {
    'pl': 'pl_core_news_lg',
    'en': 'en_core_web_trf'
}


class NERModel(object):
    def __init__(self, language, disable_pipes=False):
        assert language in MODELS_DICT
        self.nlp = spacy.load(MODELS_DICT[language])
        if disable_pipes:
            self.nlp.select_pipes(enable=NER_PIPE)

    @classmethod
    def load(cls, model_path):
        cls.nlp = spacy.load(model_path)

    def update(self, annotations, text):
        example = Example.from_dict(self.nlp.make_doc(text), annotations)
        self.nlp.update([example])

    def predict(self, text):
        pass

    def to_disk(self, path):
        self.nlp.to_disk(path)
