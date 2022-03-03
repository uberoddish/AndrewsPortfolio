from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from forms import ContactForm
import smtplib
import os

SECRET_KEY = os.environ["SECRET_KEY"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
ckeditor = CKEditor(app)
Bootstrap(app)

my_email = EMAIL
my_password = PASSWORD

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact-me', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=email,
                                to_addrs=my_email,
                                msg=f"subject:{name} has sent you an email: {subject}\n\n"
                                    f"{message}")

        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


#Hex code link: https://colorhunt.co/palette/e9e9e5d4d6c89a9b9452524e
