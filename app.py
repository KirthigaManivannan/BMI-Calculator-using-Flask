from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    bmi = calculate_bmi_value(weight, height)
    category = get_bmi_category(bmi)

    return render_template('result.html', bmi=bmi, category=category)

def calculate_bmi_value(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal Weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

if __name__ == '__main__':
    app.run(debug=True)
