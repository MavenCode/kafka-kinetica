### KineticaDB system Setup (ZSH Console 1)

`cd kinetica-component` folder

0. docker-compose down & docker system prune -a
1. docker-compose build
2. docker-compose up


### Setup the Kafka Client (ZSH Console 2)

{Download Kafka from https://www.apache.org/dyn/closer.cgi?path=/kafka/2.4.1/kafka_2.12-2.4.1.tgz =rename=> kafka-client}
0. cp `connect-standalone-sink.properties` and `sink.properties` from `kinetica-component` into `kafka-client/config` folder
1. cp `kafka-2.0.0-connector-kinetica-7.0.1.3-jar-with-dependencies.jar`  from `kinetica-component` into `kafka-client/lib` folder
2. `cd kafka-client` folder
3. run `bin/connect-standalone.sh config/connect-standalone-sink.properties config/sink.properties`


### Assuming the Kinetica GPUDB is running already and you have you ratings tables created? (ZSH Console 3)

0. `cd demo` folder
1. run `python stream_ratings.py`
