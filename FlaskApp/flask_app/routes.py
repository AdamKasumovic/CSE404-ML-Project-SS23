from flask import current_app as app
from flask import render_template, redirect, request, session, url_for, copy_current_request_context, abort, Flask, flash
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
#from .utils.database.database  import database
from werkzeug.datastructures   import ImmutableMultiDict
from werkzeug.utils import secure_filename
from pprint import pprint
import json
import random
import functools
from . import socketio
import pandas as pd
import os

@app.route('/')
def root():
    return redirect('/pokemontypeprediction')


@app.route('/pokemontypeprediction')
def pokemontypeprediction():
    return render_template('pokemontypeprediction.html')


@app.route('/pokemonclassificationresult', methods = ['POST'])
def pokemonclassificationresult():
    # check if the post request has the file part
    if 'image' not in request.files:
        flash('No file part')
        return render_template('pokemontypeprediction.html')
    file = request.files['image']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected image')
        return render_template('pokemontypeprediction.html')
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('pokemonclassificationresult.html')

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r
