from flask import Flask, jsonify, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

# import functionalities
from utils.word_count import count_words
from utils.pos_tagging import pos_tag_text
from utils.keyword_extraction import extract_keywords
from utils.sentiment_analysis import analyze_sentiment


app = Flask(__name__, static_folder='static')

# configure user upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf'}

# ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to check file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# home page
@app.route('/')
def home():
    return render_template('home.html')

# upload page
@app.route('/process-text', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check file was submitted
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        # check if the file is empty
        if file.filename=='':
            return redirect(request.url)

        # check if the file is allowed
        if file and allowed_file(file.filename):
            # save file to upload folder
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # process the file based on user selected functionality
            functionality = request.form.get('functionality')
            result = process_file(filepath, functionality)

            return render_template('result.html', filename=filename, functionality=functionality, result=result)
    return render_template('bui.html')

def process_file(file_path, functionality):
    if functionality == 'word_count':
        return count_words(file_path)
    elif functionality == 'pos_tagging':
        return pos_tag_text(file_path)
    elif functionality == 'keyword_extraction':
        return extract_keywords(file_path)
    elif functionality == 'sentiment_analysis':
        return analyze_sentiment(file_path)
    else:
        return None

# automated cleanup uploaded file
# delete file  
@app.route('/delete_uploaded_file', methods=['POST'])
def delete_uploaded_file():
    # Specify the folder where uploaded files are stored
    upload_folder = app.config['UPLOAD_FOLDER']

    # Get the list of files in the folder
    files = os.listdir(upload_folder)

    # Delete each file in the folder
    for file in files:
        file_path = os.path.join(upload_folder, file)
        try:
            os.remove(file_path)
        except Exception as e:
            # Handle the exception (e.g., log it)
            print(f"Error deleting file {file_path}: {e}")

    return 'Files deleted successfully'

if __name__ == '__main__':
    app.run(debug=True)