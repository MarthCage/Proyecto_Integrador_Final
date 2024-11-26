from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#Lista para almacenar las recetas (diccionarios con nombre, tiempo y categoría)
recetas = []

#Para mostrar recetas ---------------------------------------
@app.route('/')
def index():
    return render_template('index.html', recetas=recetas)

#Post para añadir los datos de la nueva receta :] --------------------------------------
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    recipe_name = request.form.get('recipe_name')
    cooking_time = request.form.get('cooking_time')
    category = request.form.get('category')
    ingredients = request.form.get('ingredients')
    procedure = request.form.get('procedure')

    #Para comprobar si ya existe una receta, evita que se duplique
    existing_recipe = next((recipe for recipe in recetas if recipe['recipe_name'] == recipe_name), None)
    
    if recipe_name and cooking_time and category and ingredients and procedure:
        if not existing_recipe:  #Si no existe la receta, se puede agregar :]
            recetas.append({
                'recipe_name': recipe_name,
                'cooking_time': cooking_time,
                'category': category,
                'ingredients': ingredients,
                'procedure': procedure,
            })
    
    return render_template('index.html', recetas=recetas)

#Get para obtener recetas en formato jnosify ---------------------------------------------------
@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    return jsonify(recetas)

#Post para eliminar recetas ---------------------------------------------
@app.route('/delete_recipe', methods=['POST'])
def delete_recipe():
    recipe_name_to_delete = request.form.get('recipe_name_to_delete')
    
    global recetas
    recetas = [recipe for recipe in recetas if recipe['recipe_name'] != recipe_name_to_delete]
    
    return render_template('index.html', recetas=recetas)

#Inicio de aplicación ---------------------------------------------------------------
if __name__ == '__main__':
    app.run()
