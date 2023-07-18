from flask import Flask, render_template, request
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the login page
@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form data and authentication here
        # Retrieve email and password from request.form
        email = request.form['email']
        password = request.form['password']

        # Perform authentication logic, e.g., checking credentials against a database
        # Replace the example condition with your actual authentication check
        # 要在這裡串接資料庫以確認帳戶是否有在資料庫中
        if email == 'user@example.com' and password == 'password123':
            return '登入成功！'  # You can redirect to another page or return a JSON response
        else:
            return '登入失敗！帳戶不存在：（'
    return render_template('login.html')

# Route for the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle sign-up form data and user registration here
        # Retrieve name, email, birthday, and password from request.form

        

# Define API endpoints for handling data and requests

if __name__ == '__main__':
    app.run()


# Route for the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle sign-up form data and user registration here
        # For example, retrieve name, email, and password from request.form
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Perform registration logic, e.g., storing the user data in a database
        # Replace the example code with your actual user registration code
        # For now, we're just printing the data
        print(f'Name: {name}, Email: {email}, Password: {password}')
        return 'Sign-up successful!'  # You can redirect to another page or return a JSON response

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
