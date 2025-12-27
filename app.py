from flask import Flask, send_file

# Initialize Flask
# static_folder='.' tells Flask to look for images in the current directory
# static_url_path='' tells Flask to serve them from the root URL (e.g., /1.png)
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    # Serves your main HTML file
    return send_file('ulite_design.html')

@app.route('/ceiling')
def ceiling():
    return send_file('ceiling_products.html')

if __name__ == '__main__':
    app.run(debug=True)
