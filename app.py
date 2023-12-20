from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

# import functionalities
from utils.word_count import count_words
from utils.pos_tagging import pos_tag_text
from utils.keyword_extraction import extract_keywords
from utils.sentiment_analysis import analyze_sentiment

app = Flask(__name__, static_folder='static')
app.secret_key = '8sdf8932hjksdf!@#$%^&*()_+'

# configure user upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt'}

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

            wordCount = count_words(filepath)
            extractKeywords = extract_keywords(filepath)
            sentimentAnalyze = analyze_sentiment(filepath)
            posTag = pos_tag_text(filepath)
            result = [wordCount, extractKeywords, sentimentAnalyze, posTag]

            return render_template('output.html', filename=filename, result=result)
    return render_template('form_template.html')

# show privacy policy page
@app.route('/privacy-policy')
def privacy():
    return render_template('privacy_policy.html')

# show terms and conditions page
@app.route('/terms-and-conditions')
def terms():
    return render_template('terms_conditions.html')

# automated cleanup uploaded file
# delete file after closing tab
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