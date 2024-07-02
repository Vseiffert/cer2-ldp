import React, { useEffect, useState } from 'react';
import './App.css';

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

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
              <p>{capitalize(pokemon.name)}</p>
              <p>Pokedex: {pokemon.pokedex_number}</p>
              <p>
                Tipo: {capitalize(pokemon.primary_type)}
                {pokemon.secondary_type && <span> / {capitalize(pokemon.secondary_type)}</span>}
              </p>
              <p>{pokemon.description}</p> {}
            </div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;
