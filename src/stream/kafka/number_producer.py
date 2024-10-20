from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topics = ['number_producer', 'change_producer']

# produce msg to all topics
def publish_msg_to_all_clients(msg):
    for topic in topics:
        producer.send(topic, msg)

# publish messages to the topic
for _ in range(20):
    print(f'sending {_}')
    msg = f'number_producer produced: [{_}]'.encode('utf-8')
    publish_msg_to_all_clients(msg)

    # sleep for 2 second
    time.sleep(5)