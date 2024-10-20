from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topics = ['color_producer']

color_map = {
    1: "red",
    2: "green",
    3: "blue",
    4: "yellow",
    5: "white"
}

# produce msg to all topics
def publish_msg_to_all_clients(msg):
    for topic in topics:
        producer.send(topic, msg)

def get_color(number):
    mod = number % 6
    return color_map.get(mod, "black")  # Default to "black" for unknown numbers

# publish messages to the topic
for _ in range(20):
    print(f'sending {_}')

    msg = get_color(_).encode('utf-8')
    publish_msg_to_all_clients(msg)

    # sleep for 2 second
    time.sleep(5)