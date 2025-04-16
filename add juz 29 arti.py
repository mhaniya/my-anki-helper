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

print(get_translation(70, 11))
print(get_ayat(70, 11))
