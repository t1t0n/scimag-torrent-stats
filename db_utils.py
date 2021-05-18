import pymongo

def upsert_torrent_stats(url, stats):
    client = pymongo.MongoClient("mongodb://root:root@mongo:27017/")
    db = client.scimag
    db.torrent_stats.update_one({'url':url}, {'$set':{'url':url, 'seeds':stats['seeds'], 'peers':stats['peers']}}, upsert=True)
    return True

def get_torrent_stats():
    client = pymongo.MongoClient("mongodb://root:root@mongo:27017/")
    db = client.scimag
    records = db.torrent_stats.find()
    records = list(records)
    return records
