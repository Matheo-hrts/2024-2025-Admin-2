#!/usr/bin/env python
import pika
import time
import sys
import os

def connect_to_rabbitmq():
    """Keep trying to connect until RabbitMQ is ready."""
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')  # Match your service name in Docker
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("Waiting for RabbitMQ...")
            time.sleep(2)

def main():
    connection = connect_to_rabbitmq()
    channel = connection.channel()

    # Make sure the queue exists
    channel.queue_declare(queue='orders_channel')

    def callback(ch, method, properties, body):
        print(f" [x] Received: {body.decode()}", flush=True)

    # Listen on 'hello' queue and auto-acknowledge
    channel.basic_consume(
        queue='orders_channel',
        on_message_callback=callback,
        auto_ack=True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted. Exiting...')
        connection.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == '__main__':
    main()
