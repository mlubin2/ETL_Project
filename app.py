from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy import create_engine, func
import mysql_conn


app = Flask(__name__)

connection_string = (
   f"root:{mysql_conn.password}@localhost/pokemonsearch?charset=utf8")
engine = create_engine(f'mysql://{connection_string}')


def convert_to_dict(pokemonsearch, label):
    
    uniformity = name.replace(" ", "").lower()
    for pocketmonster in pokemonsearch:
        search_term = pocketmonster["name"].replace(" ", "").lower()

        if search_term == uniformity:
            return jsonify(pocketmonster)

    return jsonify({"error": f"Pokemon with name {name} not found, please check your spelling."}), 404
        


@app.route("/")
def welcome():
        """Welcome to the Pokemon API"""
        return (
            f"Welcome to the Discount, Bargin-Bin Pokedex. We're Totally Licensed to do This."
        )

@app.route("/api/v1.0/pokemonsearch/<pokemon>")
def pokemon_search_by_pokemon_name(name):
        """Fetch the Pokemon whose name matches the path variable supplied by the user, or a 404 if not."""
        
        uniformity = name.replace(" ", "").lower()
        for pocketmonster in pokemonsearch:
            search_term = pocketmonster["name"].replace(" ", "").lower()
            
            if search_term == uniformity:
                return jsonify(pocketmonster)

        return jsonify({"error": f"Pokemon with name {name} not found, please check your spelling."}), 404

if __name__ == "__main__":
    app.run(debug=True)