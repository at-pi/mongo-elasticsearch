import json
import pickle
from pymongo import MongoClient
from pymongo.cursor import CursorType
from confluent_kafka.admin import AdminClient
from confluent_kafka import Producer
from bson import Binary


def publish_message(bootstrap_servers, topic, message):
    producer = Producer({"bootstrap.servers": bootstrap_servers})
    producer.produce(topic=topic, value=message)
    producer.flush()


def topic_exists(bootstrap_servers, topic):
    admin_client = AdminClient({"bootstrap.servers": bootstrap_servers})
    topics = admin_client.list_topics().topics
    print('topics {}'.format(topics))
    exists = topic in topics
    return exists


def main():
    client = MongoClient('mongodb://localhost:27017')
    local_db = client.local
    oplog = local_db['oplog.rs']
    cursor = oplog.find({}, cursor_type=CursorType.TAILABLE_AWAIT)

    bootstrap_servers = "localhost:9092"
    topic = "mongo-oplog"

    exists = topic_exists(bootstrap_servers, topic)
    if exists:
        print(f"The topic '{topic}' exists in Kafka.")
    else:
        print(f"The topic '{topic}' does not exist in Kafka.")
        raise Exception

    while cursor.alive:
        try:
            for entry in cursor:
                print(f"{entry['op']}")
                publish_message(bootstrap_servers, topic, pickle.dumps(entry))
        except StopIteration:
            print('Stop iteration occurred, no more data')
            pass
        except Exception as e:
            print(f"An error occurred: {e}")

    client.close()


if __name__ == "__main__":
    main()
