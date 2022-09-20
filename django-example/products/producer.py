import pika, json

params = pika.URLParameters('amqps://cgjnucdu:UT8R7i3ZJK4M_wIT8F2jsAJAz7KEmnDa@rattlesnake.rmq.cloudamqp.com/cgjnucdu')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='flask', body=json.dumps(body), properties=properties)