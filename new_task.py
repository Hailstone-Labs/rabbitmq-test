import pika 
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.77'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode = pika.DeliveryMode.Persistent
            )
        )

print(f' [x] Sent {message}.')

connection.close()

