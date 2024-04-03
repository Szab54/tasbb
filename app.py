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
    # Belso IP cim lekerese
    hostname = socket.gethostname()
    internal_ip = socket.gethostbyname(hostname)
    
    # Kulso IP cim lekerese
    external_ip = socket.gethostbyname(socket.gethostname())
    
    # Flask alkalmazas inditasa mindket IP cimen
    app.run(host=internal_ip, port=8880, debug=True)
    app.run(host=external_ip, port=8880, debug=True)

