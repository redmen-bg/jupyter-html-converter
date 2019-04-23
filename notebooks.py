import tempfile
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
from files import create_temp_file, write_to_file
import jupyter_client

def convert_to_html_file(notebook_path):
    with(open(notebook_path, "r")) as notebook_file:
        notebook_data = _read_notebook(notebook_file)
        _execute_notebook(notebook_data)
        html = _convert_notebook_to_html(notebook_data)

        notebook_html_file = create_temp_file()
        write_to_file(html, notebook_html_file)

        return notebook_html_file

def _read_notebook(notebook_file):
    notebook_data = notebook_file.read()
    notebook = nbformat.reads(notebook_data, as_version=4)

    return notebook

def _execute_notebook(notebook_data):

    from jupyter_client.kernelspec import KernelSpecManager
    km = KernelSpecManager()
    print('> find_kernel_specs <')
    print(km.find_kernel_specs())

    print('-- get_kernel_spec --')
    print(km.get_kernel_spec("python3").to_dict())

    preprocessor = ExecutePreprocessor(timeout=600, kernel_name='python3')
    preprocessor.preprocess(notebook_data, {'metadata': {'path': tempfile.gettempdir()}})

def _convert_notebook_to_html(notebook_data):
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
    body, _ = html_exporter.from_notebook_node(notebook_data)

    return body



