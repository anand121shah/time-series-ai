from flask import Flask
from routes.main import main

app = Flask(__name__)
app.secret_key = 'replace_with_a_secure_random_key'

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
