from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')
'''
cluster = "mongodb+srv://mylesmgrxnt:W3stern317!@cluster0.sufd5.mongodb.net/CRUD?retryWrites=true&w=majority"

client = MongoClient(cluster)

db = client.CRUD

crudcollect = db.crudcollect

item = {"name": "Midterms", "place": "Merkert Center"}

retrieve = crudcollect.find_one()

crudcollect.insert_one(item)

print(retrieve)
'''
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)