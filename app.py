from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'une_cle_secrete'

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/produits')
def produits():
    return render_template('produits.html')

@app.route('/ajouter', methods=['POST'])
def ajouter_au_panier():
    nom = request.form['nom']
    prix = float(request.form['prix'])

    if 'panier' not in session:
        session['panier'] = []

    session['panier'].append({'nom': nom, 'prix': prix})
    return redirect(url_for('produits'))

@app.route('/panier')
def panier():
    panier = session.get('panier', [])
    total = sum(item['prix'] for item in panier)
    return render_template('panier.html', panier=panier, total=total)

if __name__ == '__main__':
    app.run(debug=True)