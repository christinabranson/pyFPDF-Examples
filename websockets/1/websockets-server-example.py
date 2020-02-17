# WS server example

import asyncio
import websockets
import os
from weasyprint import HTML, CSS
import base64


async def makepdf(websocket, path):
    name = await websocket.recv()
    HTML(string=name).write_pdf('pdfs/testing_from_webservice.pdf')
    message = "writing pdf with " + name +"?"
    print(f"< {message}")


start_server = websockets.serve(makepdf, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()