from flask import Flask, render_template, request
import requests

app = Flask(__name__)
BACKEND_URL = "http://127.0.0.1:5000/data_types"


@app.get("/")
def get_index():
    response = requests.get(BACKEND_URL)
    scan_data = response.json().get("data_types")
    return render_template("index.html", data_types=scan_data)


@app.get("/summary")
def get_summary():
    response = requests.get(BACKEND_URL)
    scan_data = response.json().get("data_types")
    return render_template("summary.html", data_types=scan_data)


@app.get("/about")
def get_about():
    return render_template("about.html")


@app.get("/integer")
def get_integer():
    url = "%s/%s" % (BACKEND_URL, "integer")
    response = requests.get(url)
    integer_data = response.json().get("data_type")
    return render_template("data_type.html", data_type=integer_data[0])


@app.get("/float")
def get_float():
    url = "%s/%s" % (BACKEND_URL, "float")
    response = requests.get(url)
    float_data = response.json().get("data_type")
    return render_template("data_type.html", data_type=float_data[0])


@app.get("/boolean")
def get_boolean():
    url = "%s/%s" % (BACKEND_URL, "boolean")
    response = requests.get(url)
    boolean_data = response.json().get("data_type")
    return render_template("data_type.html", data_type=boolean_data[0])


@app.get("/string")
def get_string():
    url = "%s/%s" % (BACKEND_URL, "string")
    response = requests.get(url)
    string_data = response.json().get("data_type")
    return render_template("data_type.html", data_type=string_data[0])


@app.get("/list")
def get_list():
    url = "%s/%s" % (BACKEND_URL, "list")
    response = requests.get(url)
    list_data = response.json().get("data_type")
    return render_template("data_type.html", data_type=list_data[0])


@app.get("/dictionary")
def get_dictionary():
    url = "%s/%s" % (BACKEND_URL, "dictionary")
    response = requests.get(url)
    dictionary_data = response.json().get("data_type")
    return render_template("data_type.html", data_type=dictionary_data[0])


@app.get("/tuple")
def get_tuple():
    url = "%s/%s" % (BACKEND_URL, "tuple")
    response = requests.get(url)
    tuple_data = response.json().get("data_type")
    return render_template("data_type.html", data_type=tuple_data[0])


@app.get("/create/data_types")
def get_data_type_form():
    return render_template("new.html")


@app.post("/create/data_types")
def create_data_type():
    form_data = request.form
    new_dt = {
        "name": form_data.get("name"),
        "summary": form_data.get("summary"),
        "description": form_data.get("description")
    }
    response = requests.post(BACKEND_URL, json=new_dt)
    if response.status_code == 204:
        return render_template("new_success.html")
    else:
        return render_template("failed.html")