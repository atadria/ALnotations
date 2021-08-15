import streamlit as st

from model.language import MODELS_DICT
from model.model import NERModel

TITLE = "ALnotations"
DEFAULT_MODEL = 'en_core_web_md'
DEFAULT_TEXT = 'David Bowie moved to the US in 1974, initially staying in New York City before settling in Los Angeles.'
MODEL_NAMES = MODELS_DICT.keys()


def visualize():
    st.sidebar.title(TITLE)

    # model selection
    spacy_model = st.sidebar.selectbox("Model",
                                       MODEL_NAMES,
                                       format_func=str)

    # load model
    nlp = NERModel(spacy_model)

    text = st.text_area("Text to analyze", DEFAULT_TEXT)

visualize()
