import woody
import pika
import time
import sys
import os

def connect_to_rabbitmq():
    """Keep trying to connect until RabbitMQ is ready."""
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("Waiting for RabbitMQ...")
            time.sleep(2)

# #### 4. internal Services
def process_order(order_id, order):
    # ...
    # ... do many check and stuff
    status = woody.make_heavy_validation(order)

    woody.save_order(order_id, status, order)

def main():
    connection = connect_to_rabbitmq()
    channel = connection.channel()

    channel.queue_declare(queue='orders_channel')

    def callback(ch, method, properties, body):
        message = json.loads(body)
        order_id = message['order_id']
        order_product = message['order_product']
        print(f" [x] Received: order id = {prder_id}, order product = {order_product}", flush=True)
        process_order(order_id, order_product)

    channel.basic_consume(
        queue='orders_channel',
        on_message_callback=callback,
        auto_ack=True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)
    channel.start_consuming()


if __name__ == "__main__":
    main()
