#!/usr/bin/env python3

"""
This is a very simple script to send a WebSocket message.
Badge: HTTP Badge
Task: 43
"""

import websockets
import asyncio

async def send_message():
    async with websockets.connect('ws://ptl-33ef39d2-5e9494c7.libcurl.so/pentesterlab') as ws:
        message = 'key'
        await ws.send(message)
        response = await ws.recv()
        print(f"{response}")

asyncio.run(send_message())
