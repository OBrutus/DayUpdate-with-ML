from pymongo import collection
from pymongo import MongoClient


## CHANGE THIS WHEN IN PRODUCTION ##
DATABASE_NAME = "news"
CONNECTION_STRING = "mongodb://localhost:27017/"
####################################

CURRENT_SOURCE = "gktoday"

URL_NAME = "https://www.sunnyskyz.com/good-news/"
META_COLLECTION_NAME = "meta_stories"


## Metrics ##
update_attempts = 0
db_read_failure = 0
db_write_failure = 0
successful_updates = 0


### Filters ###
URL_FILTER = {
    "url": URL_NAME,
}

def get_database_collection(
        collection_name: str
) -> collection.Collection:
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    if DATABASE_NAME not in client.list_database_names():
        print('Check the database name ' + DATABASE_NAME + ' is not present')
    # Create the database for our example (we will use the same database throughout the tutorial
    return client[DATABASE_NAME][collection_name]


def get_article_number(
        mongo_collection: collection.Collection
) -> int:
    document = mongo_collection.find_one(
        URL_FILTER
    )
    return document['last_recorded'] + 0


def set_article_number(
        mongo_collection: collection.Collection,
        article_number: int
) -> bool:
    global update_attempts
    global db_write_failure

    article_number = article_number + 1
    print('Updating the last recorded article number to {}'.format(article_number))
    try:
        update_attempts += 1
        mongo_collection.update_one(
            URL_FILTER,
            {
                "$set": {'last_recorded': article_number}
            }
        )
    except Exception as e:
        db_write_failure += 1
        print('Failed to write to db', e)
        return False

    print('Updated the last recorded article number to {}'.format(article_number))
    return True


def raw_file_store(
    title: str,
    data: str
) -> int:
    raw_file = open(title, 'w')
    written_chars = raw_file.write(data)
    raw_file.close()
    return written_chars


def raw_file_read(
    file_location: str
) -> str:
    raw_text = open(file_location, 'r')
    return raw_text.read()
