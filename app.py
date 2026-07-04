from flask import Flask,request,render_template
from src.Pipelines.prediction_pipeline import PredictPipeline
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    if request.method == 'POST':
        male = request.form['male']
        age = int(request.form['age'])
        education=int(request.form.get('education',0))
        currentSmoker = request.form['currentSmoker']
        cigsPerDay = float(request.form['cigsPerDay'])
        BPMeds = request.form['BPMeds']
        prevalentStroke = request.form['prevalentStroke']
        prevalentHyp = request.form['prevalentHyp']
        diabetes = request.form['diabetes']
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = float(request.form['heartRate'])
        glucose = float(request.form['glucose'])
        implement=PredictPipeline()
        prediction = implement.predict( male, age, education,currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP,BMI,heartRate,glucose)
        prediction_text = "The Patient has Heart Disease" if prediction == 1 else "The Patient has No Heart Disease"

        return render_template('index.html', prediction=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)