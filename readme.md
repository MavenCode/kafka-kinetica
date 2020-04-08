

Setup Instructions
==================

0. git clone this repo

1. cp the kinecta connector jar generated from your `mvn clean package` of 
   `https://github.com/kineticadb/kinetica-connector-kafka`  inside this directory

2. do `docker-compose up -d` to start the kafka, zookeeper, kagent, gpudb-head, gpudb-worker

3. to stop do `docker-compose down` to stop the kafka, zookeeper, kagent, gpudb-head, gpudb-worker


Quick Kafka Debugging Steps
============================
1. Create Topic on Kafka:
`bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic <TopicName>` 

for sanity sake do `bin/kafka-topics.sh --list --bootstrap-server localhost:9092` to make sure Topic was created

2. Post Test Message to the Topic in JSON format
`bin/kafka-console-producer.sh --broker-list localhost:9092 --topic <TopicName>`  

3. Consume Message from the Topic in JSON format
`bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <TopicName> --from-beginning`


Minor Test messages
===================
`bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1  --topic Tweets.KafkaConnectorTest0`

{ "created_at": "Wed Oct 10 20:19:24 +0000 2018", "id": 25, "text": "Hello World, Testing Kinetica Abi!" }

* https://github.com/kineticadb/kinetica-connector-kafka

* test to see if Kafka is running `netstat -an|grep 9092`


> 8iKdUZ6YY233-kgX7yJHrEZ8w-kLQx4Utq+rOr-SZeQRHlO0OOd-p4qmH7m6gFXDMP4A8Q5P9+5lk9CxJD4g