from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            age=int(request.form.get('age')),
            sex=int(request.form.get('sex')),
            bmi=float(request.form.get('bmi')),
            children=int(request.form.get('children')),
            smoker=int(request.form.get('smoker')),
            region=int(request.form.get('region'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('index.html', results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0")