import spacy

MODELS_DICT = {
    'pl': 'pl_core_news_md',
    'en': 'en_core_web_md'
}


def load_model(language):
    if language in MODELS_DICT:
        return spacy.load(MODELS_DICT[language])
    else:
        raise NotImplementedError('No model for language: {}'.format(language))
