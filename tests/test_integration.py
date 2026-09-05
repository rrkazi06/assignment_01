"""Integration tests — drive each interface end-to-end.

Each interface imports the same bill.py module, so these confirm the module is
wired correctly into the console, notebook, and Streamlit front-ends.
"""

import nbformat
from nbclient import NotebookClient
from streamlit.testing.v1 import AppTest

from helpers import run_python_script


def test_console_app():
    # Feed subtotal=50, tip=20%, people=4 to the console app on stdin.
    output = run_python_script("./code/console.py", "50\n20\n4\n")
    assert "$10.00" in output   # tip
    assert "$60.00" in output   # grand total
    assert "$15.00" in output   # per person
    assert "generous" in output.lower()


def test_notebook_app():
    # Execute the notebook headless (kernel runs in code/ so `import bill` works).
    nb = nbformat.read("code/explore.ipynb", as_version=4)
    NotebookClient(nb, resources={"metadata": {"path": "code"}}).execute()
    printed = "\n".join(
        out.get("text", "")
        for cell in nb.cells if cell.cell_type == "code"
        for out in cell.get("outputs", [])
    )
    assert "15.0" in printed     # $50 bill, 20% tip, split 4 ways


def _widget(widgets, key):
    for widget in widgets:
        if getattr(widget, "key", None) == key:
            return widget
    raise KeyError(key)


def test_streamlit_app():
    app = AppTest.from_file("code/dashboard.py")
    app.run()
    _widget(app.number_input, "subtotal").set_value(50.0)
    _widget(app.slider, "tip").set_value(20)
    _widget(app.number_input, "people").set_value(4)
    app.run()

    assert not app.exception
    metrics = {m.label: m.value for m in app.metric}
    assert metrics["Tip"] == "$10.00"
    assert metrics["Grand total"] == "$60.00"
    assert metrics["Per person"] == "$15.00"
