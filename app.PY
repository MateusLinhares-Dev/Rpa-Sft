from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
import re

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist('file[]')
    new_filenames = []

    for file in uploaded_files:
        filename = secure_filename(file.filename)
        new_filename = remove_special_characters(filename)
        file.save(os.path.join('uploads', new_filename))
        new_filenames.append(new_filename)

    return render_template('download.html', filenames=new_filenames)

def remove_special_characters(filename):
    # Remove special characters from the filename
    return re.sub(r'[^\w\s.-]', '', filename)

@app.route('/download/<filename>')
def download(filename):
    path = os.path.join('uploads', filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
