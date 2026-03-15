import os
from webdriver_manager.chrome import ChromeDriverManager

os.environ["WEBDRIVER_CHROME_DRIVER"] = ChromeDriverManager().install()
from app import app

def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Pink Morsel Sales Visualiser"

def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None

def test_region_filter_is_present(dash_duo):
    dash_duo.start_server(app)
    region_filter = dash_duo.find_element("#region-filter")
    assert region_filter is not None