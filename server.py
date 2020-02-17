# WS server example

import json
import asyncio
import websockets
import os
from weasyprint import HTML, CSS
import base64

def validate_json(json_data):
    print(f"> Validating JSON...")
    # make sure that the required field is set
    required_fields = [
        "template",
        "outputpath",
        "filename",
        "title",
        "text",
    ]

    for required_field in required_fields:
        try:
            if len(json_data[required_field]) > 0:
                print(f"> {required_field}: {json_data[required_field]}")
            else:
                return False
        except IndexError:
            return False

    # todo make sure template is either ss or st

    return True

def validate_path_writeable(path):
    if os.access(path, os.W_OK):
        return True

    return False

def get_html(json_data):
    # open template file
    root = os.path.dirname(os.path.abspath(__file__))
    htmlpath = os.path.join(root, 'templates', '5_test_complicated_template_with_arguments.html')
    with open(htmlpath, 'r') as file:
        html = file.read()

        # replace spots in text with pre-defined values
        html = html.replace("{% title %}", json_data["title"])
        html = html.replace("{% text %}", json_data["text"])

        return html

    return ""

def get_output_filename(json_data):
    return os.path.join(json_data["outputpath"],json_data["filename"])

async def makepdf(websocket, path):
    json_data_from_socket = await websocket.recv()
    json_data = json.loads(json_data_from_socket)

    # send message letting them know that the request was recieved
    await websocket.send("Received request to generate PDF...")

    # check on json
    if not validate_json(json_data):
        await websocket.send("Error: Error in JSON")
    else:
        if not validate_path_writeable(json_data["outputpath"]):
            await websocket.send("Error: Requested path is not writeable")
        else:
            html = get_html(json_data)

            HTML(string=html).write_pdf(get_output_filename(json_data))
            await websocket.send("PDF Generated at " + json_data["outputpath"] + json_data["filename"])

start_server = websockets.serve(makepdf, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()