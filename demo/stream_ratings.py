from json import dumps
from kafka import KafkaProducer
import csv, time

KAFKA_TOPIC="ratingtopic0"
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:dumps(x).encode('utf-8'))
with open('ratings_with_headers_20m.csv') as ratings_csv_file:
    read_csv = csv.reader(ratings_csv_file, delimiter=',')
    row_index=0
    for row in read_csv:
        if row_index != 0:
            data = { 'userId': int(row[0]), 'movieId': int(row[1]), 'rating': float(row[2]), 'ts': int(row[3]) }
            print("Sending number to Kafka", data)
            producer.send(KAFKA_TOPIC, value=data)
            producer.flush()
            time.sleep(0.1)
        row_index = row_index + 1

