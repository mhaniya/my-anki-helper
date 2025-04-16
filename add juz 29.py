import http.client
import json

def add_notes(sound_file, image_files: list, ayat):
    conn = http.client.HTTPConnection("localhost", 8765)
    back = ""
    for image in image_files:
        back = back + f"<img src=\"{image}\">"
    payload = json.dumps({
    "action": "addNote",
    "version": 6,
    "params": {
        "note": {
        "deckName": "Juz 29",
        "modelName": "Basic",
        "fields": {
            "Front": f"[sound:{sound_file}]",
            "Back": back,
            "Detail": f"{ayat}"
        },
        "options": {
            "allowDuplicate": False,
            "duplicateScope": "deck"
        },
        "tags": [
            "Al-Haqqah"
        ]
        }
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def store_media(ayat_number):
    conn = http.client.HTTPConnection("localhost", 8765)
    payload = json.dumps({
    "action": "storeMediaFile",
    "version": 6,
    "params": {
        "filename": f"070{"{:03d}".format(ayat_number)}.mp3",
        "path": f"D:\\Temp File\\Juz 29\\Al Maarij\\070{"{:03d}".format(ayat_number)}.mp3"
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_str = data.decode("utf-8")
    print(json_str)
    res_data = json.loads(json_str)
    return res_data["result"]

for i in range(2, 45):
    media_file = store_media(i)
    image_files = []
    if i <= 10:
        image_files = ["CamScanner%2004-10-2025%2005.32.jpg", "Juz 29 halaman 569.jpg"]
    elif i <= 39:
        image_files = ["Juz 29 halaman 569.jpg", "Juz 29 halaman 570.jpg"]
    else: 
        image_files = ["Juz 29 halaman 570.jpg"]
    add_notes(f"070{"{:03d}".format(i)}.mp3", image_files, f"Al Maarij: {i}")