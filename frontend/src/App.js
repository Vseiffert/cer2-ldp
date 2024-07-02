import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [pokemonList, setPokemonList] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/pokemons/')
      .then(response => response.json())
      .then(data => {
        setPokemonList(data);
      })
      .catch(error => {
        console.error('Error fetching Pokemon data:', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Pokémon List</h1>
        <div className="pokemon-list">
          {pokemonList.map(pokemon => (
            <div key={pokemon.pokedex_number} className="pokemon-item">
              <img src={pokemon.image_url} alt={pokemon.name} />
              <p>{pokemon.name}</p>
              <p>Type: {pokemon.primary_type}</p>
              {pokemon.secondary_type && <p>Secondary Type: {pokemon.secondary_type}</p>}
            </div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;

