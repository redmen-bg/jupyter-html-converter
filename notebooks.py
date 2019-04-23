import nbformat
from nbconvert import HTMLExporter
from files import create_temp_file, write_to_file
import jupyter_client

def convert_to_html_file(notebook_path):
    with(open(notebook_path, "r")) as notebook_file:
        notebook_data = _read_notebook(notebook_file)
        html = _convert_notebook_to_html(notebook_data)
        
        notebook_html_file = create_temp_file()
        write_to_file(html, notebook_html_file)

        return notebook_html_file

def _read_notebook(notebook_file):
    notebook_data = notebook_file.read()
    notebook = nbformat.reads(notebook_data, as_version=4)

    return notebook

def _convert_notebook_to_html(notebook_data):
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
    body, _ = html_exporter.from_notebook_node(notebook_data)

    return body

    

