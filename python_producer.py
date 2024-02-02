import json
import time
import random
from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def produce_messages(producer, topic, key, value):
    try:
        # Produce the message to Kafka
        producer.produce(topic, key=key, value=value, callback=delivery_report)

        # Wait for any outstanding messages to be delivered and delivery reports received.
        producer.flush()

        # Introduce a delay between messages (adjust as needed)
        time.sleep(1)

    except KeyboardInterrupt:
        print("User interrupted the process. Shutting down gracefully.")

def main():
    # Set up producer configuration
    conf = {
        'bootstrap.servers': 'localhost:29092',
        'client.id': 'python-producer-test'
    }

    # Create a Kafka producer instance
    producer = Producer(conf)

    # Topic to which the producer will send messages
    topic = 'test_topic'

    try:
        for _ in range(10):
            random_integer = random.randint(1, 10)
            # Example: Start producing continuous messages with a specific key and value
            key = 'your_key'
            value = {'message': 'Hello, Kafka!', 'timestamp': time.time(), 'quantity': random_integer}
            produce_messages(producer, topic, key, json.dumps(value))

    except Exception as e:
        print('Error in the main loop: {}'.format(e))

if __name__ == '__main__':
    main()
