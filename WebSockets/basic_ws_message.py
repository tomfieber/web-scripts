#!/usr/bin/env python3

"""
This is a very simple script to send a WebSocket message.
Badge: HTTP Badge
Task: 43
"""

import websockets
import asyncio

async def send_message():
    location = input("Please enter the address of the websocket: ")
    async with websockets.connect(location) as ws:
        message = input("What message do you want to send? ")
        await ws.send(message)
        response = await ws.recv()
        print(f"{response}")

asyncio.run(send_message())
