
from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup
from dockerplace import app
from dockerplace.system_calls import get_all_actions


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/desktop')
def desktop():
    """
    this route displays a list of available services to the user
    """
    return render_template(
        "desktop.html",
        services=get_all_actions(app.config["DOCKER_SERVICES_HOME"])
        )


@app.route('/service/action')
def service_action_runner():
    return render_template(
        "console.html",
        data={"some": "thing"}
        )


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
        if valid_login(
                request.form['username'],
                request.form['password']
                ):
            return log_user_in(request.form['username'])
        else:
            error = "Invalid username/password!"
    return render_template('login.html', error=error)
