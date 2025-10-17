import asyncio
import time
from lazy_socket.server import LazyServer
from websockets import client


class Server(LazyServer):

    async def process_message(self, client, message):
        await client.send(f"{self.name}:echo:{message}")

if __name__ == "__main__":
    server = Server(name="TestServer", host="0.0.0.0", port=5000, version="1.0")

    try:
        server.start()
    except KeyboardInterrupt:
        print("Shutting down server...")