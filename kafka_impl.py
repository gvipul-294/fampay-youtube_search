from kafka import KafkaProducer, KafkaConsumer
import os
import json

# Kafka settings
KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC')

# producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, 
#                         # value_serializer=lambda v: json.dumps(v).encode('utf-8'),
#                         # max_request_size=20971520,
#                         api_version = (2, 0, 2))

# consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
