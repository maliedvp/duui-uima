# https://www.reichstagsprotokolle.de/Band2_w2_bsb00000065.html

# uvicorn duui-parliament-segmenter:app --reload

import requests
import re

with open('/Users/marli453/develop/duui_files/1924/' + '10._Sitzung_24.06.1924.xmi.gz.txt', 'r') as file:
# with open('/Users/marli453/develop/duui_files/1924/' + '18._Sitzung_25.07.1924.xmi.gz.txt', 'r') as file:
    text = file.read()

# print(text)

response = requests.post("http://127.0.0.1:8000/v1/process", json={
    "doc_len": len(text),
    "lang": "de",
    "text": text,
    "subtitle": "2. Wahlperiode"
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

# print(data.keys())
no_speeches = len(data["speeches"])
len_speaker = len(data["speakers"])

# Now access elements
print(f"\n\nSpeeches: {no_speeches}")
for idx,speech in enumerate(data["speeches"]):
    if idx <= 5:
        print(f"\t{speech}")


print(f"\n\nSpeakers: {len_speaker}")
for idx,speaker in enumerate(data["speakers"]):
    if idx <= 5:
        print(f"\t{speaker}")


# New output:
if no_speeches == len_speaker:
    for idx,speech in enumerate(data["speeches"]):
        print(idx)
        print(
            'SPEAKER', 
            data["speakers"][idx]['name'], '  |  ', data["speakers"][idx]['party'], '  |  ', data["speakers"][idx]['party_deducted'], '  |  ', data["speakers"][idx]['fullname_deducted'], '  |  ', data["speakers"][idx]['label']
        )
        speech_begin = data["speeches"][idx]['begin']
        print('SPEECH', re.sub(r'\n','',text[speech_begin:speech_begin+50]))
        print('--------------------------------------------')

        # if idx ==5:
        #     break


