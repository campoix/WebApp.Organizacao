from flask import render_template, Flask

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")

@app.route("/")
def index():
    return render_template('beta_final.html')
@app.route("/sobre")
def sobre():
    return "Feito por: Enzo Campoi estudante, feito em python, css, html "

if __name__=='__main__':
    app.run(debug = True)