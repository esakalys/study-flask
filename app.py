from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginattempt', methods=['POST'])
def verify():
    email = request.form.get('email')
    password = request.form.get('pass')
    return(render_template('success.html', password=password, email=email))

@app.route('/register')
def register():
    return render_template('register.html')



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
