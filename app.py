from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'static'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No image selected')
        return redirect(url_for('hello_world'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No image selected')
        return redirect(url_for('hello_world'))
    
    if file and file.filename and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash(f'Image "{filename}" uploaded successfully to static folder!')
        return redirect(url_for('hello_world'))
    else:
        flash('Invalid file type. Please upload an image (png, jpg, jpeg, gif, bmp, webp)')
        return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
