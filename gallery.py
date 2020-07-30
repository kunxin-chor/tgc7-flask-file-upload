import json
import uuid

database = {}


def save():
    global database
    print(database)
    with open('db.json', 'w') as filehandler:
        json.dump(database, filehandler)


def load():
    global database
    with open('db.json', 'r') as filehandler:
        database = json.load(filehandler)


def get_database():
    global database
    return database


def put(asset_id, url, caption):
    global database
    image_id = str(uuid.uuid1())
    image = {
        "id": image_id,
        "asset_id": asset_id,
        "url": url,
        "caption": caption
    }
    database[image_id] = image


def update(image_id, asset_id, url, caption):
    global database
    image = {
        "id": image_id,
        "asset_id": asset_id,
        "url": url,
        "caption": caption
    }
    database[image_id] = image


def get_image(asset_id):
    global database
    return database[asset_id]
