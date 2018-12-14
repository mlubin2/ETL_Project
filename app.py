from flask import Flask, jsonify, render_template
from mysql_conn import password as passw
import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password = passw,
                             db='pokemonsearch',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)

#connection_string = (
#   f"root:{mysql_conn.password}@localhost/pokemonsearch?charset=utf8")
#engine = create_engine(f'mysql://{connection_string}')

#session = Session(engine)


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

@app.route("/api/v1.0/pokemonsearch/<name>")
def pokemon_search_by_pokemon_name(name):
        """Fetch the Pokemon whose name matches the path variable supplied by the user, or a 404 if not."""
        print(name)
        name = name.lower() 
        name = name.strip(" ")

        try:
            with connection.cursor() as cursor:
                #sql = "select * from pokedex where LOWER(pokedex.Name) ='"+name+"'"
                sql = "select * from pokedex LEFT JOIN pokemongo ON pokedex.id = pokemongo.id where LOWER(pokedex.Name) ='"+name+"'"
                print(sql)
                cursor.execute(sql)
                pokemonsearch = cursor.fetchall()
                print(type(pokemonsearch))
                for pocketmonster in pokemonsearch:
                    
                    search_term = pocketmonster["Name"].replace(" ", "").lower()
                    return jsonify(pocketmonster)
                    
                    
        except:
            pass
        return jsonify({"error": f"The Pokemon you've searched for was not found, please check your spelling."}), 404
            
             

if __name__ == "__main__":
    app.run(debug=True)