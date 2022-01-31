import flask
import pickle

with open(f'model/linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template(template_name_or_list='index.html'))

    if flask.request.method == 'POST':
        number_courses = flask.request.form['number_courses']
        time_study = flask.request.form['time_study']

        number_courses = float(number_courses)
        time_study = float(time_study)

        input_variables = [[number_courses, time_study]]
        prediction = model.predict(input_variables)[0]
        prediction = round(prediction, 2)

        return flask.render_template(template_name_or_list='index.html', result=prediction)


if __name__ == '__main__':
    app.run()
