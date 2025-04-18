# uvicorn duui-parliament-segmenter:app --reload

import requests
import re


with open('1._Sitzung_27.05.1924.xmi.gz.txt', 'r') as file:
	text = file.read()

# print(text)

response = requests.post("http://127.0.0.1:8000/v1/process", json={
    "doc_len": len(text),
    "lang": "de",
    "text": text
})

# Print status and response for debugging
print("Status Code:", response.status_code)
# print("Response Text:", response.text)

# Try to parse only if it's valid JSON
if response.headers.get("Content-Type") == "application/json":
    pass
else:
    print("⚠️ Response was not JSON.")

data = response.json()

# Now access elements
print("\n\nSpeeches:")
for idx,speech in enumerate(data["speeches"]):
	print(f"\t{speech}")

print("\n\nSpeakers:")
for idx,speaker in enumerate(data["speakers"]):
	print(f"\t{speaker}")



