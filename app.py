from flask import Flask, render_template

# Initialize Flask
# static_folder='.' allows serving images/css from the root folder
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return render_template('ulite_design.html')

@app.route('/ceiling')
def ceiling():
    return render_template('ceiling_products.html')

@app.route('/wall')
def wall():
    # Placeholder: Re-using home or ceiling until you build a wall page
    return render_template('ulite_design.html')

@app.route('/ground')
def ground():
    return render_template('ulite_design.html')

@app.route('/gallery')
def gallery():
    return render_template('ulite_design.html')

@app.route('/support')
def support():
    return render_template('ulite_design.html')

@app.route('/product')
def product():
    return render_template('product_detail.html')

if __name__ == '__main__':
    app.run(debug=True)
