import spacy_streamlit

from model.language import MODELS_DICT

DEFAULT_MODEL = 'en_core_web_md'
DEFAULT_TEXT = 'David Bowie moved to the US in 1974, initially staying in New York City before settling in Los Angeles.'
MODELS = {v: k for k, v in MODELS_DICT.items()}
DESCRIPTION = 'DESCRIPTION'


def get_default_text(nlp):
    return DEFAULT_TEXT


spacy_streamlit.visualize(
    MODELS,
    default_model=DEFAULT_MODEL,
    visualizers=['parser', 'ner', 'similarity', 'tokens'],
    show_visualizer_select=True,
    sidebar_description=DESCRIPTION,
    get_default_text=get_default_text
)
