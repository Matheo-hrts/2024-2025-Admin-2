#!/usr/bin/env python
import pika
import time

while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq')
        )
        break
    except pika.exceptions.AMQPConnectionError:
        print("Waiting for RabbitMQ...")
        time.sleep(2)

channel = connection.channel()
channel.queue_declare(queue='orders_channel')
channel.basic_publish(exchange='', routing_key='orders_channel', body='Initialise queue')
print(" [x] Sent 'Initialize queue'")
connection.close()
