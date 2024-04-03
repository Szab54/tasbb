from flask import Flask
import requests

# Flask alkalmazás létrehozása
app = Flask(__name__)

# Alapértelmezett útvonal definiálása
@app.route('/')
def hello_world():
    return 'Hello, World! This is a Flask App.'

# Egy másik útvonal definiálása
@app.route('/about')
def about():
    return 'About page'

# Főprogram: Flask alkalmazás indítása
if __name__ == '__main__':
    public_ip = requests.get('https://api.ipify.org').text
    print(f"Public IP Address: {public_ip}")
    app.run(host=public_ip, port=8880)
