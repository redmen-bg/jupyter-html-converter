import nbformat
from nbconvert import HTMLExporter

def convert_to_html(notebook):
    with(open(notebook, "r")) as notebook_file:
        notebook = _read_notebook(notebook_file)
        html = _convert_notebook_to_html(notebook)
        
        return html

def _read_notebook(notebook_file):
    notebook_data = notebook_file.read()
    notebook = nbformat.reads(notebook_data, as_version=4)

    return notebook

def _convert_notebook_to_html(notebook):
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
    body, _ = html_exporter.from_notebook_node(notebook)

    return body

