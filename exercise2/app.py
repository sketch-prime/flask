from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('result', number=request.form.get('number')))
    return render_template('form.html')

@app.route('/result')
def result():
    number = request.args.get('number')
    result = determine_number_type(number)
    return render_template('result.html', number=number, result=result)

def determine_number_type(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return 'even'
        else:
            return 'odd'
    except (ValueError, TypeError):
        return 'not an integer'

if __name__ == '__main__':
    app.run(debug=True)