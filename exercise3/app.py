from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Hardcoded student organizations
student_organizations = {
    "Organization 1",
    "Organization 2",
    "Organization 3",
    "Organization 4",
    "Organization 5"
}

registered_users = {}

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        
        # Backend validation
        if name and organization in student_organizations:
            registered_users[name] = organization
            return redirect(url_for('registered_users_page'))
        else:
            return "Invalid input. Please provide a valid name and organization."
    
    return render_template('register.html', student_organizations=student_organizations)

@app.route('/registered_users')
def registered_users_page():
    return render_template('registered_users.html', registered_users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)