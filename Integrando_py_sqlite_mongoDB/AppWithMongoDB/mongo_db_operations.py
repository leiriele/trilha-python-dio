import datetime
import pprint
import pymongo

try:
    client = pymongo.MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER_URL>/test?retryWrites=true&w=majority")
    db = client.test
    posts = db.posts
except pymongo.errors.ConnectionFailure:
    print("Erro ao conectar ao MongoDB")
    exit()

post = {
    "author": "Leiriele",
    "text": "Integrando Python com SQLite e MongoDB",
    "tags": ["mongodb", "dio", "pymongo"],
    "date": datetime.datetime.utcnow()
}

post_id = posts.insert_one(post).inserted_id
print("ID POST:", post_id)

print("\n Documento recuperado:")
pprint.pprint(posts.find_one())

new_posts = [
    {
        "author": "Leiriele",
        "text": "Post Leiriele",
        "title":"Primeiro",
        "tags": ["pymongo", "post"],
        "date": datetime.datetime.utcnow()
    },
    {
        "author": "Maria",
        "text": "Post teste Maria",
        "title": "Desafio Pymongo",
        "date": datetime.datetime(2023, 15, 30, 05, 45)
    },
    {
        "author": "Jorginho",
        "text": "Gosto muito de desafios",
        "title": "Desafio",
        "date": datetime.datetime(2023, 20, 30, 05, 45)
    }

]

result = posts.insert_many(new_posts)
print("\n IDs dos posts inseridos:", result.inserted_ids)


print("\n Recuperação por autor (Maria):")
pprint.pprint(posts.find_one({"author": "Maria"}))

print("\n Recuperação por titulo (Maria):")
pprint.pprint(posts.find_one({"title": "Desafio"}))

print("\n Post encontrados na coleção: ")
for post in posts.find():
    pprint.pprint(post)
