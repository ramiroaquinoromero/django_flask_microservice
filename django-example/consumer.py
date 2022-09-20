import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_example.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://cgjnucdu:UT8R7i3ZJK4M_wIT8F2jsAJAz7KEmnDa@rattlesnake.rmq.cloudamqp.com/cgjnucdu')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='django_example')


def callback(ch, method, properties, body):
    print('Received in Django Example')
    print(body)
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='django_example', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()