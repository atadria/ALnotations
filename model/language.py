import spacy

MODELS_DICT = {
    'pl': 'pl_core_news_md',
    'en': 'en_core_web_md',
    'de': 'de_core_news_md',
    'fr': 'fr_core_news_md',
    'es': 'es_core_news_md',
    'it': 'it_core_news_md',
    'el': 'el_core_news_md',
    'xx': 'xx_ent_wiki_sm'
}


def load_model(language):
    language = language.lower()
    if language in MODELS_DICT:
        return spacy.load(MODELS_DICT[language])
    else:
        raise NotImplementedError('No model for language: {}'.format(language))
