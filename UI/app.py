from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
bootstrap = Bootstrap(app)

class ChatForm(FlaskForm):
    user_input = StringField('Enter your message:', validators=[DataRequired()])
    submit = SubmitField('Send')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ChatForm()
    if form.validate_on_submit():
        user_input = form.user_input.data
        # Process user_input and generate a response from your chatbot here
        response = user_input #TEMP
        flash(response, 'bot_response')
        form.user_input.data = ''
    return render_template('index.html', form=form)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Handle the file upload and server paths here
        pass
        return redirect(url_for('index'))
    return render_template('upload.html')

@app.route('/choose_material', methods=['GET', 'POST'])
def choose_material():
    if request.method == 'POST':
        # Handle the material selection here
        pass
        return redirect(url_for('index'))
    return render_template('choose_material.html')


@app.context_processor
def inject_bootstrap():
    return dict(bootstrap=bootstrap)

if __name__ == '__main__':
    app.run(debug=True)
