"""
Routes and views for the flask application.
"""
from flask import Flask,render_template,Response, redirect, url_for, request, session, abort

app = Flask(__name__)


class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]


app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/docapps')


@app.route('/')
def index():
    """Renders the home page."""
    return render_template(
        'login.html',
        title='login page'
)


@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='My Details'
    )


@app.route('/bank')
def bank():
    """Renders the bank page."""
    return render_template(
        'bank.html',
        title='bank',
        message='Your bank details.'
    )


@app.route('/card')
def card():
    """Renders the card page."""
    return render_template(
        'card.html',
        title='card',
        message='Your card details.'
    )


@app.route('/social')
def social():
    """Renders the social media page."""
    return render_template(
        'social.html',
        title='social media',
        message='Your social media description page.'
    )


@app.route('/family')
def family():
    """Renders the family page."""
    return render_template(
        'familyDetails.html',
        title='familyDetails',
        message='Your familyDetails description page.'
    )


@app.route('/education')
def education():
    """Renders the education page."""
    return render_template(
        'education.html',
        title='educationDetails',
        message='Your educationDetails description page.'
    )


@app.route('/documents')
def documents():
    """Renders the documents page."""
    return render_template(
        'document.html',
        title='documentDetails',
        message='Your documentDetails description page.'
    )


@app.route('/proof')
def proof():
    """Renders the id proof page."""
    return render_template(
        'proof.html',
        title='proofDetails',
        message='Your proof Details description page.'
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['Username']
        if request.form['Username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
