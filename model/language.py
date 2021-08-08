import spacy

MODELS_DICT = {
    'pl': 'pl_core_news_lg',
    'en': 'en_core_web_trf'
}


def load_model(language):
    if language in MODELS_DICT:
        return spacy.load(MODELS_DICT[language])
    else:
        raise NotImplementedError('No model for language: {}'.format(language))
