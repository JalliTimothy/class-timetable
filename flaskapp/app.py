from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        # Simple credential checking
        if username.lower() == 'admin' and password == 'Admin@123':
            flash('Welcome Admin!', 'success')
            return redirect(url_for('admin_dashboard'))
        elif password == 'Teacher@123':
            flash('Welcome Teacher!', 'success')
            return redirect(url_for('teacher_dashboard'))
        elif username == password:
            flash('Welcome Student!', 'success')
            return redirect(url_for('student_dashboard'))
        else:
            flash('Invalid credentials! Please try again.', 'error')
            return redirect(url_for('home'))
    else:
        flash('Both fields are required!', 'error')
        return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        rollno = request.form.get('rollno')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        course = request.form.get('course')
        branch = request.form.get('branch')
        year = request.form.get('year')

        # Simple confirmation without database
        flash(f'Registration successful for {name}!', 'success')
        return redirect(url_for('home'))

    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)
