from flask import Flask

haijaya = Flask(__name__)
@haijaya.route("/")
def display():
    return "Hai This is an end to end project"


if __name__ == "__main__":
    haijaya.run(host = "0.0.0.0" , port = int("5000"), debug=True)

