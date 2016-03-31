from pymongo import MongoClient
import star_realms_cards

client = MongoClient()
db = client.starrealms

db.cards.insert(star_realms_cards.StarRealmsCards.BASE_SET)
