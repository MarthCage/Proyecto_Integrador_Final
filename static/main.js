document.addEventListener('DOMContentLoaded', function () {
    const formBtn = document.getElementById('add_btn'); //Botón para ir al formulario
    const backBtn = document.getElementById('back-btn'); //Botón para volver
    const formSection = document.getElementById('formulario_recipes'); //Sección de formulario
    const recipesSection = document.getElementById('list_card_recipes'); //Sección de recetas
    const searchInput = document.getElementById('buscar'); //Búsqueda

    //Función para cambiar de recetas a formulario -----------------------------
    formBtn.addEventListener('click', function () {
        formSection.style.display = 'block';
        recipesSection.style.display = 'none';
    });

    //Función para cambiar de formulario a recetas -------------------------------
    backBtn.addEventListener('click', function () {
        formSection.style.display = 'none';
        recipesSection.style.display = 'block';
    });

    // Función para filtrar recetas por categoría ----------------------------
    window.filterRecipes = function (category) {
        const recipes = document.querySelectorAll('.card_recipe');
        recipes.forEach(recipe => {
            if (category === 'all' || recipe.dataset.category === category) {
                recipe.style.display = 'block';
            } else {
                recipe.style.display = 'none';
            }
        });
    };

    //Función para filtrar recetas por nombre -------------------------------------------------------
    searchInput.addEventListener('input', function () {
        const searchTerm = searchInput.value.toLowerCase();
        const recipes = document.querySelectorAll('.card_recipe');

        recipes.forEach(recipe => {
            const recipeName = recipe.querySelector('h3').textContent.toLowerCase();
            if (recipeName.includes(searchTerm)) {
                recipe.style.display = 'block';
            } else {  
                recipe.style.display = 'none';
            }
        });
    });
});