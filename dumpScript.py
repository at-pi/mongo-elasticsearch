import pymongo
import random
import uuid

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

myDB = myClient["dumpdb"]
eventLogCol = myDB["event_logs"]
objectMappingCol = myDB["object_mapping"]

totalRowsInserted = 0
numberOfRecords = random.randint(10000, 10001)

for i in range(0, numberOfRecords):
    x = uuid.uuid1()

    id = "id_{}"
    id = id.format(x)
    meeting_id = "meeting_{}"
    meeting_id = meeting_id.format(x)
    presentation_id = "presentation_{}"
    presentation_id = presentation_id.format(x)
    duration = random.randint(100,999)

    myDict = { "id": id, "meeting_id": meeting_id, "presentation_id": presentation_id, "duration": duration }
    eventLogCol.insert_one(myDict)
    totalRowsInserted += 1

    call2Id = "call2_{}"
    call2Id = call2Id.format(x)
    myDict = {"meeting_id": meeting_id, "call2_id": call2Id}
    objectMappingCol.insert_one(myDict)
    totalRowsInserted += 1
    print("inserted - {}".format(meeting_id))

print(myClient.list_database_names())
print(myDB.list_collection_names())
print("total rows inserted - {}".format(totalRowsInserted))