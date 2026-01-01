from flask import Flask, render_template, abort

app = Flask(__name__, static_folder='.', static_url_path='')

# --- 1. THE PRODUCT DATABASE ---
CATALOG = {
    "suspended": {
        "track-head": [
            {"name": "Suspended Track Pro", "aperture": "3inch", "lumens": "800lm", "env": "Dry Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Suspended+Track"},
            {"name": "Zoom Pendant", "aperture": "4inch", "lumens": "1200lm", "env": "Dry Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Zoom+Pendant"}
        ],
        "cylinder": [
            {"name": "Cylinder Slim", "aperture": "2inch", "lumens": "1000lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Cylinder+Slim"},
            {"name": "Cylinder Max", "aperture": "6inch", "lumens": "3000lm", "env": "Wet Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Cylinder+Max"}
        ],
        "linear": [
            {"name": "Line X1", "aperture": "1.5inch", "lumens": "800lm/ft", "env": "Dry Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Line+X1"}
        ],
        "acoustic": [
            {"name": "Sound Absorb A", "aperture": "N/A", "lumens": "1500lm", "env": "Dry Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Acoustic+Panel"}
        ],
        "decorative-pendant": [
            {"name": "Deco Sphere", "aperture": "12inch", "lumens": "1800lm", "env": "Dry Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Deco+Sphere"}
        ]
    },
    "recessed": {
        "round-downlight": [
            {"name": "Super 3inch Adjustable", "aperture": "2inch", "lumens": "640~1700lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Super+3+Adjustable"},
            {"name": "Super 4inch Fix", "aperture": "4inch", "lumens": "800~1600lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Super+4+Fix"},
            {"name": "Wino 6inch Fix", "aperture": "6inch", "lumens": "1600~3200lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Wino+6+Fix"},
            {"name": "Lux 6inch Fix", "aperture": "6inch", "lumens": "1800~4800lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Lux+6+Fix"},
            {"name": "Glaxy 8inch", "aperture": "8inch", "lumens": "3200~6400lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Glaxy+8"},
            {"name": "Max 10inch Fix", "aperture": "10inch", "lumens": "3200~8000lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Max+10+Fix"}
        ],
        "square-downlight": [
            {"name": "Square 4", "aperture": "4inch", "lumens": "1000lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Square+4"}
        ],
        "trimless-downlight": [
            {"name": "Invisible 3", "aperture": "3inch", "lumens": "900lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Invisible+3"}
        ],
        "magnetic-track": [
            {"name": "Mag Track 24V", "aperture": "1inch", "lumens": "Varies", "env": "Dry Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Mag+Track"}
        ],
        "linear": [
            {"name": "Recessed Line", "aperture": "2inch", "lumens": "1000lm/ft", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Recessed+Line"}
        ],
        "troffer": [
            {"name": "Office Panel 2x2", "aperture": "2x2", "lumens": "4000lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Troffer+2x2"}
        ]
    },
    "surface": {
        "track-head": [
            {"name": "Surface Spot", "aperture": "3inch", "lumens": "1100lm", "env": "Dry Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Surface+Spot"}
        ],
        "cylinder": [
            {"name": "Surface Can", "aperture": "4inch", "lumens": "1500lm", "env": "Wet Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Surface+Can"}
        ],
        "trimless-downlight": [
            {"name": "Surface Smooth", "aperture": "4inch", "lumens": "1200lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Surface+Smooth"}
        ],
        "linear": [
            {"name": "Surface Strip", "aperture": "2inch", "lumens": "950lm/ft", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Surface+Strip"}
        ],
        "magnetic-track": [
            {"name": "Surface Mag", "aperture": "1.5inch", "lumens": "Varies", "env": "Dry Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Surface+Mag"}
        ],
        "panel": [
            {"name": "Cloud Panel", "aperture": "2x4", "lumens": "5000lm", "env": "Damp Rated", "img": "https://placehold.co/500x500/e0e0e0/333?text=Cloud+Panel"}
        ]
    }
}

@app.route('/')
def home():
    return render_template('ulite_design.html')

# --- 2. "EXPLORE ALL" ROUTE (Aggregates Products) ---
@app.route('/ceiling/<category>')
def ceiling_category(category):
    # Get all subcategories for this main category
    category_data = CATALOG.get(category, {})
    
    # Combine all lists into one big list of products
    all_products = []
    for subcat_list in category_data.values():
        all_products.extend(subcat_list)
    
    # Send the combined list to the template
    return render_template('ceiling_products.html', 
                           products=all_products, 
                           cat_name=category, 
                           sub_name="All Models")

# --- 3. SPECIFIC SUBCATEGORY ROUTE ---
@app.route('/ceiling/<category>/<subcategory>')
def ceiling_subcategory(category, subcategory):
    # Lookup the products in the CATALOG based on the URL
    products = CATALOG.get(category, {}).get(subcategory, [])
    
    return render_template('ceiling_products.html', 
                           products=products, 
                           cat_name=category, 
                           sub_name=subcategory)

@app.route('/ceiling')
def ceiling():
    # Default redirect
    return ceiling_subcategory('recessed', 'round-downlight')

# --- 4. PRODUCT DETAIL ROUTE (Robust Search Fix) ---
@app.route('/product/<product_name>')
def product(product_name):
    selected_product = None
    
    # 1. Normalize the search term (lowercase, remove spaces)
    # This fixes issues where "Super%203inch" doesn't match "Super 3inch"
    search_term = product_name.lower().replace(' ', '').replace('%20', '')

    # 2. Search the entire catalog
    for cat in CATALOG.values():
        for sub in cat.values():
            for p in sub:
                # Normalize the catalog name too
                catalog_name = p['name'].lower().replace(' ', '')
                
                # Compare the "clean" versions
                if catalog_name == search_term:
                    selected_product = p
                    break
            if selected_product: break
        if selected_product: break
    
    if selected_product is None:
        abort(404)
        
    return render_template('product_detail.html', product=selected_product)

# --- 5. PLACEHOLDER ROUTES ---
@app.route('/wall')
def wall():
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

if __name__ == '__main__':
    app.run(debug=True, port=8000)

