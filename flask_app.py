from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return  '<body> <marquee> Welcome  to  my Website-http://nishabuzz.pythonanywhere.com</marquee> </body>'
app.run()