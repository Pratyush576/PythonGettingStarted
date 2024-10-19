from kafka import KafkaConsumer
from termcolor import colored


consumers = ['number_producer', 'change_producer', 'color_producer']
# consume messages published to number_consumer topics
consumer = KafkaConsumer('number_consumer')



#for msg in consumer:
#    print(msg)


# Create a Kafka consumer that listens to multiple topics
consumer = KafkaConsumer(
    *consumers,  # Unpack the list of topics
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Start reading at the earliest available message
    enable_auto_commit=True,       # Auto-commit message offsets
    group_id='my-group',           # Consumer group id
    value_deserializer=lambda x: x.decode('utf-8')  # Deserialize message values
)

# Consume messages
try:
    for message in consumer:
        if(message.topic == 'number_producer'):
            color = 'yellow'
        elif(message.topic == 'color_producer'):
            color = 'green'
        else:
            color = 'white'
        print(colored(f"Received message from topic: {message.topic}, Message value: {message.value}", color))
finally:
    # Close the consumer
    consumer.close()