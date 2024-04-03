from flask import Flask

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
    app.run(port=8880)  # Az alkalmazás debug módjának beállítása

