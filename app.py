from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html' )

@app.route("/process", methods=['GET','POST'])
def process():

    if request.method == 'POST':

        query = request.form['query']         
        predictin = process_model(query)

    return render_template('result.html', query=query ,predictin=predictin)


def process_model(query):

    model_class= ['carros', 'economia', 'educacao', 'esporte', 'musica', 'politica']

    model = load("./modelo/classificador_model.joblib")

    predict = model.predict([query])

    predictin = model_class[predict[0]]

    return predictin

if __name__ == "__main__":
    app.run(debug=True)