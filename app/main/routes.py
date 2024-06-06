# app/main/routes.py
from app.main import bp

from flask import render_template, request, redirect, url_for, flash
from flask import current_app as app
# from flask_socketio import SocketIO, send
from werkzeug.utils import secure_filename
import os

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home', paths = [])


@app.route('/button-clicked', methods=['POST'])
def button_clicked():
    # Your Python code goes here
    return 'Button clicked!'


# @bp.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash('No selected file')
#         return redirect(request.url)
#     if file:
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
#         flash(f'File successfully uploaded to {file_path}')
#         return redirect(url_for('main.index'))


# @bp.route('/setpath', methods=['GET', 'POST'])
# def set_path():
#     paths = []
#     if request.method == 'POST':
#         new_path = request.form['path']
#         if new_path:
#             return None
        
#     return render_template('index.html')