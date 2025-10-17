from lazy_socket.client import LazyClient

client = LazyClient()
client.start()

while True:
    if client.queue.empty():
        continue

    message = client.queue.get()
    if message.startswith("lazy_client:connected:"):
        client.send("Hello, Lazy Server!")