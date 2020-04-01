

Setup Instructions

1. cp the kinecta connector jar generated from your build inside this directory
2. do `docker-compose up -d` to start the kafka and zookeeper
3. to stop do `docker-compose down`



test zookeeper topic -> bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test


bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic  Tweets.KafkaConnectorTest

bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic Tweets.KafkaConnectorTest2




1. Create Topic on Kafka:
`bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic <TopicName>` 

for sanity sake do `bin/kafka-topics.sh --list --bootstrap-server localhost:9092` to make sure Topic was created

2. Post Test Message to the Topic in JSON format
`bin/kafka-console-producer.sh --broker-list localhost:9092 --topic <TopicName>`  

3. Consume Message from the Topic in JSON format
`bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <TopicName> --from-beginning`



#netstat -an|grep 9092


bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1  --topic Tweets.KafkaConnectorTest0

{ "created_at": "Wed Oct 10 20:19:24 +0000 2018", "id": 25, "text": "Hello World, Testing Kinetica Abi!" }

* https://github.com/kineticadb/kinetica-connector-kafka