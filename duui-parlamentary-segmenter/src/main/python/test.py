# uvicorn duui-parliament-segmenter:app --reload

import requests
import re

text = """Präsident: Das Wort hat der Herr Reichsjustizminister.
Dr. Heinze, Reichsminister der Justiz: Meine Herren,
ich habe keine Bedenken gegen die von dem Herrn Vorredner
gestellten Anträge. Ich habe namentlich auch keine
Bedenken gegen die Abänderung des Art. III, da es sich
in dieser Beziehung nicht um Eingriffe in die Exekutive
handelt.
Präsident: Weitere Wortmeldungen liegen nicht
vor; ich schließe die allgemeine Aussprache.
Ich rufe in der besonderen Beratung auf den Art. I
mit den Abänderungsanträgen, die der Herr Abgeordnete
Giebel eben begründet hat.
Ich bitte diejenigen Damen und Herren, welche den
Abänderungsanträgen Giebel, Kaiser, Molkenbuhr, Karsten
zum Art. I zustimmen wollen, sich vom Platz zu erheben.
(Geschieht.)
Das Wort hat der Herr Berichterstatter Abgeordneter
Dr. Hertz.
Dr. Hertz, Abgeordneter, Berichterstatter: Meine
Herren! Dem Ausschüsse lagen außer der Vorlage der
Regierung auch die Initiativanträge Müller (Franken)
und Genossen und Dr. Helfferich und Genossen vor. Den
Beratungen wurde die Regierungsvorlage zugrunde gelegt.
In der allgemeinen Aussprache kündigte der Reichs-
finanzminister einige Gesetzentwürfe an, durch die die
Steuergesetzgebung in dreierlei Beziehung geändert werden
soll. Erstens soll die beschleunigte Einziehung der Steuern
Im Monat September: Gesamtaufkommen der Einkommen- (0)
steuer 13 8 Milliarden, L'hn- und Gehaltsabzug etwa
8,1 Milliarden gleich 58,33 Prozent.
Kahmann, Abgeordneter: Meine Damen und Herren!
Als das Einkommensteuergesetz im Juli dieses Jahres M)
geändert wurde, konnte allerdings kein Mensch voraussehen,
daß der Wert der Mark in so rasendem Tempo
nach unten stürzen würde. Der Dollar stand damals fünfhundert,
also auf dem Hundertzwanzigfachen; die Teuerung
war ungefähr sechzigfach, und die Lohnsteigerung mochte
ungefähr das Vierzigfache im allgemeinen ausmachen. Jetzt
pendelt der Dollar um achttausend herum;"""

text = re.sub(r'\s*\n\s*', ' ', text)
text = re.sub(r'\s{2,}', ' ', text).strip()

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



