const fetch = require("node-fetch");
const fs = require('fs');

function getPokemon(){
    fetch('https://pokeapi.co/api/v2/pokemon?limit=151')
    .then(response => response.json())
    .then(allpokemon => {
        allpokemon = allpokemon.results;
        let pokemon = allpokemon.map(function(item){
            return item.name;
        })
        fs.writeFile('pokemon.txt', pokemon, (err) => {
            if (err) throw err;
        })
    });
    
}

getPokemon();