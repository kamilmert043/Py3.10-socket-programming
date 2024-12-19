import websockets
import asyncio

clients = []


async def proxy(websocket):
    try:
        print("Connected")
        clients.append(websocket)
        async for message in websocket:
            print("Received message:", message)
            websockets.broadcast(clients, message)

    finally:
        clients.remove(websocket)


async def main():
    async with websockets.serve(proxy, "localhost", 2708):
        await asyncio.Future()


asyncio.run(main())