

Setup Instructions

1. cp the kinecta connector jar generated from your build inside this directory
2. do `docker-compose up -d` to start the kafka and zookeeper
3. to stop do `docker-compose down`




# test zookeeper topic -> bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test


bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic  Tweets.KafkaConnectorTest

bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic Tweets.KafkaConnectorTest2