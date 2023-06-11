import pymongo
from pymongo import MongoClient
from pymongo.cursor import CursorType

client = MongoClient('mongodb://localhost:27017')

# Execute the replSetGetStatus command
# result = client.admin.command('replSetGetStatus')

# Check the number of replica sets
# num_replica_sets = len(result['members'])
# print("Number of replica sets:", num_replica_sets)

local_db = client.local
oplog = local_db['oplog.rs']
cursor = oplog.find({}, cursor_type=CursorType.TAILABLE_AWAIT)

while cursor.alive:
    try:
        for entry in cursor:
            print(entry)
    except StopIteration:
        print('stop iteration occured no more data')
        pass
    except Exception as e:
        print(f"An error occurred: {e}")

client.close()





