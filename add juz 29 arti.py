import http.client
import json

def get_translation(no_quran, no_ayat):
    conn = http.client.HTTPConnection("api.alquran.cloud")
    payload = ''
    headers = {}
    conn.request("GET", f"/v1/ayah/{no_quran}:{no_ayat}/id.indonesian", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))["data"]["text"]

def get_ayat(no_quran, no_ayat):
    conn = http.client.HTTPConnection("api.alquran.cloud")
    payload = ''
    headers = {}
    conn.request("GET", f"/v1/ayah/{no_quran}:{no_ayat}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))["data"]["text"]

def add_notes(surah_name, ayat_number, arabic_text, translate):
    conn = http.client.HTTPConnection("localhost", 8765)
    payload = json.dumps({
    "action": "addNote",
    "version": 6,
    "params": {
        "note": {
        "deckName": "Juz 29 Arti",
        "modelName": "Basic",
        "fields": {
            "Front": arabic_text,
            "Back": translate,
            "Detail": f"{surah_name}: {ayat_number}"
        },
        "options": {
            "allowDuplicate": False,
            "duplicateScope": "deck"
        },
        "tags": [
            surah_name
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

for i in range(12, 45):
    translate = get_translation(70, i)
    arabic_text = get_ayat(70, i)
    add_notes("Al-Maarij", i, arabic_text, translate)
