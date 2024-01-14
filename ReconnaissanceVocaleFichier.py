#!/usr/bin/env python3

petitM = "vosk-model-small-fr-0.22"
grosM = "vosk-model-fr-0.22"
SAMPLE_RATE = 48000
fichiersAanalyses = "*.mp4"
fRapport = "fRapport"

import subprocess
import glob
import json
import conversionNombre as convNb
import os

from vosk import Model, KaldiRecognizer, SetLogLevel

SetLogLevel(0)

model = Model(model_name=grosM)
rec = KaldiRecognizer(model, SAMPLE_RATE)

f = open(fRapport+".txt", 'w',encoding="utf-8")
cTot=0
cTrv=0

for fichier in glob.glob(fichiersAanalyses, recursive=True):
    cTot+=1
    retour = ""
    print (fichier)
    f.write(fichier+"\n")
    with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                                fichier,
                                "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                                stdout=subprocess.PIPE) as process:

        while True:
            data = process.stdout.read(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                # print(rec.Result())
                structureJson = json.loads(rec.Result())
                paroles = ""
                paroles = structureJson['text']
                if ((paroles.find("plan") != -1) or (paroles.find("pri") != -1)):
                    cTrv+=1
                    retour = convNb.idPrise(paroles)
                    print(paroles + " -> " + retour)
                    f.write(paroles + " -> " + retour +"\n")
                    break
    # Changement de nom du fichier
    if (retour.find("S") !=-1):
        iMp4=fichier.find(".MP4")
        nouvNom=fichier[:iMp4]+"_"+retour+".MP4"
        os.rename(fichier,nouvNom)
            # else:
            #     print(rec.PartialResult())

        # print(rec.FinalResult())
f.close()

print("\nNb de lignes trouve " + str(cTrv) + " nb de fichier mp4 " + str(cTot))