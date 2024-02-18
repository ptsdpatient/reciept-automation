import http.client
import json

conn = http.client.HTTPSConnection("ppveqe.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "from": "447860099299",
            "to": "918459291118",
            "messageId": "8469253a-3cd6-41c7-ad25-e983a4425fdd",
            "content": {
                "templateName": "message_test",
                "templateData": {
                    "body": {
                        "placeholders": ["Tanishq"]
                    }
                },
                "language": "en"
            }
        }
    ]
})
headers = {
    'Authorization': 'App 7dc756931e7a9e5fe2dc3f935cf51e9e-7b0d44d3-9b23-40cb-b0e3-3e436152a73c',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/whatsapp/1/message/template", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))