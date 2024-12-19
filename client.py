import websockets
import asyncio
import threading

msg_list = []


async def add_msgs_to_list(ws):
    async for msg in ws:
        msg_list.append(msg)


async def proxy(websocket):
    global msg_list
    while True:
        for msg in msg_list:
            msg_list.remove(msg)
            print("Received message:", msg)

        await websocket.send(input("Enter message: "))


async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        t = threading.Thread(target=asyncio.run, args=(add_msgs_to_list(websocket),))
        t.start()
        await proxy(websocket)


asyncio.run(main())