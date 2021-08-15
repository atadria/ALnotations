import dash
import dash_html_components as html
import dash_core_components as dcc
from spacy.displacy.render import DEFAULT_LABEL_COLORS

from model.model import NERModel

MODEL_LABELS = [{'label': 'Polish', 'value': 'pl'},
                {'label': 'English', 'value': 'en'}]

# Initialize the application
app = dash.Dash(__name__)


def ent_name(name):
    return html.Span(name, style={
        "font-size": "0.8em",
        "font-weight": "bold",
        "line-height": "1",
        "border-radius": "0.35em",
        "text-transform": "uppercase",
        "vertical-align": "middle",
        "margin-left": "0.5rem"
    })


def ent_box(children, color):
    return html.Mark(children, style={
        "background": color,
        "padding": "0.2em 0.2em",
        "margin": "0 0.2em",
        "line-height": "1",
        "border-radius": "0.35em",
    })


def entity(children, name):
    if type(children) is str:
        children = [children]

    children.append(ent_name(name))
    color = DEFAULT_LABEL_COLORS[name]
    return ent_box(children, color)


def render(doc):
    children = []
    last_idx = 0
    for ent in doc.ents:
        children.append(doc.text[last_idx:ent.start_char])
        children.append(
            entity(doc.text[ent.start_char:ent.end_char], ent.label_))
        last_idx = ent.end_char
    children.append(doc.text[last_idx:])
    return children


nlp_model = NERModel('en')


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('model-selection-dropdown', 'value')])
def update_output(value):
    return 'Selected language {}'.format(value)


model_selection = dcc.Dropdown(id='model-selection-dropdown',
                               options=MODEL_LABELS,
                               value='en')

model_selection_output = html.Div(id='dd-output-container')

text = 'David Bowie moved to the US in 1974, initially staying in New York City before settling in Los Angeles.'
doc = nlp_model.process(text)

# define the app
app.layout = html.Div([model_selection,
                       model_selection_output,
                       *render(doc)])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
