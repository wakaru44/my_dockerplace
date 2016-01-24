
from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup
import helpers
from dockerplace import app

@app.route('/event', defaults={"path": ""})
@app.route('/event/<path:whatever>')
def event_listener(whatever):
    app.logger.info(whatever)
    """
    The format of the URL should be something like 

    - SessionID: GUID (or a string for the purpose of this demo)
    - Timestamp: Int. The unix timestamp in the client
    - Client Version: String. Something to identify the version/kind/variation of the client
    - Item: String. The thing that the user has touched. 

    In this order, and validating a bit
    """
    (sesid, stamp, client, item) = parse_request(whatever)
    assert sessionid_check(sesid) is not False
    assert stamp_check(stamp) is not False
    assert client_check(client) is not False
    assert item_check(item) is not False
    return "{0} registered".format(whatever)


@app.route('/')
def index():
    return "You are at the homepage!"

    

@app.route('/redirect-to-<function>')
def pointless_redirect(function=None):
    return redirect(url_for(function))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']

@app.route('/login', methods=['GET', 'POST'])
def login_handler():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                        request.form['password']):
            return log_user_in(request.form['username'])
        else:
            error = "Invalid username/password!"
    return render_template('login.html', error=error)


