import pymongo
import pprint

db = pymongo.MongoClient("licalhost", 27017)

test = db.test.poost

doc = test.find_one({"name" : "text"})

pprint.pprint(doc)