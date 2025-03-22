import os

def create_folders():
    folders = [
        'static/css', 'static/js', 'static/images', 'templates', 'routes', 'models', 'utils'
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def create_files():
    files = {
        'app.py': """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
""",
        'routes/__init__.py': '',
        'routes/main.py': """from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')
""",
        'models/__init__.py': '',
        'utils/__init__.py': '',
        'static/css/style.css': """body { font-family: Arial, sans-serif; background-color: #f4f4f4; }""",
        'templates/index.html': """<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Time Series AI</title>
    <link rel='stylesheet' href='{{ url_for('static', filename='css/style.css') }}'>
</head>
<body>
    <h1>Welcome to Time Series AI</h1>
</body>
</html>""",
    }
    
    for file, content in files.items():
        with open(file, 'w') as f:
            f.write(content)

def main():
    create_folders()
    create_files()
    print("Project structure initialized successfully.")

if __name__ == "__main__":
    main()
