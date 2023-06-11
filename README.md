# Tail mongodb's oplog and send message to kafka

step 1: install mongodb, kafka use brew for this 

step 2: mongo started standalone if replication is not mentioned in conf file.
        add replication and name of replica set in `/usr/local/etc/mongod.conf` (adding replicaset is important because only then oplog will be crated to replicate data into other non-primary nodes)

step 3: start mongo using brew services start monogodb-community

step 4: run dumpScript to dump random data to monogodb

step 5: create topic in kafka using -> `kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

step 6: run tailOplog script to read oplog one by one using a tailable cursor and publish message to kafka

