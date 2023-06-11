import pymongo
import random
import uuid

client = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = client["dumpdb"]
event_log_col = my_db["event_logs"]
object_mapping_col = my_db["object_mapping"]

total_rows_inserted = 0
number_of_records = random.randint(100, 200)

for i in range(0, number_of_records):
    x = uuid.uuid1()

    id = "id_{}"
    id = id.format(x)
    meeting_id = "meeting_{}"
    meeting_id = meeting_id.format(x)
    presentation_id = "presentation_{}"
    presentation_id = presentation_id.format(x)
    duration = random.randint(100, 999)

    my_dict = {"id": id, "meeting_id": meeting_id, "presentation_id": presentation_id, "duration": duration}
    event_log_col.insert_one(my_dict)
    total_rows_inserted += 1

    call2_id = "call2_{}"
    call2_id = call2_id.format(x)
    my_dict = {"meeting_id": meeting_id, "call2_id": call2_id}
    object_mapping_col.insert_one(my_dict)
    total_rows_inserted += 1
    print("{} - inserted - {}".format(total_rows_inserted, meeting_id))

print(client.list_database_names())
print(my_db.list_collection_names())
print("total rows inserted - {}".format(total_rows_inserted))
