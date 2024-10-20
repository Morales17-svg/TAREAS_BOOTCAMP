const apiKey = '6c38302aaae8d49e371b2a14a8d6fa12'; // Reemplaza con tu clave API
const apiUrl = 'https://api.themoviedb.org/3';
const movieList = document.getElementById('movies');
const movieDetails = document.getElementById('movie-details');
const detailsContainer = document.getElementById('details');
const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');
const favoritesList = document.getElementById('favorites-list');
const addToFavoritesButton = document.getElementById('add-to-favorites');
const trailerButton = document.getElementById('trailer-button');
let selectedMovieId = null;
let favoriteMovies = JSON.parse(localStorage.getItem('favorites')) || [];

// Fetch and display popular movies
async function fetchPopularMovies() {
    try {
        const response = await fetch(`${apiUrl}/movie/popular?api_key=${apiKey}&language=es-ES`);
        const data = await response.json();
        displayMovies(data.results);
    } catch (error) {
        console.error('Error fetching popular movies:', error);
    }
}

// Display movies
function displayMovies(movies) {
    movieList.innerHTML = ''; // Limpia la lista de películas
    movies.forEach(movie => {
        const li = document.createElement('li');
        li.innerHTML = `
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}">
            <span>${movie.title}</span>
        `;
        li.onclick = () => showMovieDetails(movie.id); // Muestra detalles al hacer clic en la película
        movieList.appendChild(li);
    });
}

// Show movie details
async function showMovieDetails(movieId) {
    try {
        const response = await fetch(`${apiUrl}/movie/${movieId}?api_key=${apiKey}&language=es-ES`);
        const movie = await response.json();
        
        detailsContainer.innerHTML = `
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}">
            <h3>${movie.title}</h3>
            <p>${movie.overview}</p>
            <p>Fecha de lanzamiento: ${movie.release_date}</p>
        `;

        selectedMovieId = movieId; // Guarda el ID de la película seleccionada

        // Aquí puedes agregar la lógica para el botón de tráiler
        trailerButton.onclick = () => watchTrailer(movieId);
        
        movieDetails.classList.remove('hidden'); // Muestra la sección de detalles
    } catch (error) {
        console.error('Error fetching movie details:', error);
    }
}

// Watch trailer
async function watchTrailer(movieId) {
    try {
        const response = await fetch(`${apiUrl}/movie/${movieId}/videos?api_key=${apiKey}&language=es-ES`);
        const videos = await response.json();
        const trailer = videos.results.find(video => video.type === 'Trailer'); // Busca el tráiler
        if (trailer) {
            window.open(`https://www.youtube.com/watch?v=${trailer.key}`, '_blank'); // Abre el tráiler en una nueva pestaña
        } else {
            alert('No hay tráiler disponible para esta película.');
        }
    } catch (error) {
        console.error('Error fetching trailer:', error);
    }
}

// Search movies
searchButton.addEventListener('click', async () => {
    searchMovies();
});

// Allow searching with Enter key
searchInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        searchMovies();
    }
});

async function searchMovies() {
    const query = searchInput.value;
    if (query) {
        try {
            const response = await fetch(`${apiUrl}/search/movie?api_key=${apiKey}&language=es-ES&query=${encodeURIComponent(query)}`);
            const data = await response.json();
            displayMovies(data.results);
        } catch (error) {
            console.error('Error searching movies:', error);
        }
    }
}

// Add movie to favorites
addToFavoritesButton.addEventListener('click', () => {
    if (selectedMovieId) {
        const favoriteMovie = {
            id: selectedMovieId,
            title: document.querySelector('#details h3').textContent
        };
        if (!favoriteMovies.some(movie => movie.id === selectedMovieId)) {
            favoriteMovies.push(favoriteMovie);
            localStorage.setItem('favorites', JSON.stringify(favoriteMovies)); // Guarda en localStorage
            displayFavorites(); // Muestra la lista actualizada de favoritos
        }
    }
});

// Display favorite movies
function displayFavorites() {
    favoritesList.innerHTML = ''; // Limpia la lista de favoritos
    favoriteMovies.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        favoritesList.appendChild(li);
    });
}

// Initial fetch of popular movies and display favorites
fetchPopularMovies(); // Obtiene y muestra las películas populares
displayFavorites(); // Muestra las películas favoritas guardadas
