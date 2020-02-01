#!/usr/bin/env python3
from urllib.request import urlopen
import time
import datetime


#Configuration
fileURL = "http://storage.vsi.esdm.go.id/monitoring/CCTV/TangkubanParahu/Latest/cam_1.jpg"
downloadDelay = 30
errorDelay = 2
downloadTimeout = 5
fileOutput = "./result/file_"
fileExtension = ".jpg"
#End of Configuration


now = datetime.datetime.now()
seqnum = int(input("Starting Number: "))
hashstore = ""

while True: #Main Loop
    try: #Downloading the file
        filedata = urlopen(fileURL, timeout=downloadTimeout)
        datatowrite = filedata.read()

        if hashstore != str(hash(datatowrite)): #Saving the file
            with open(fileOutput + str(seqnum) + fileExtension, 'wb') as f:
                f.write(datatowrite)
                seqnum = seqnum + 1
            print("[" + str(datetime.datetime.now()) + "] " + "Currently on sequence number: " + str(seqnum))
            hashstore = str(hash(datatowrite))
            time.sleep(downloadDelay)

        elif hashstore == str(hash(datatowrite)): #Duplicate detection
            print("[" + str(datetime.datetime.now()) + "] " + "Duplicate On Sequence Number: " + str(seqnum) + " (Hash: " + str(hash(datatowrite)) + ")" ". Skipping file")
            continue

        else: #If error while comparing hashes
            print("[" + str(datetime.datetime.now()) + "] " + "An Error Occured While Comparing hashes (Continuing Anyways). Hash: " + str(hash(datatowrite)))

    except KeyboardInterrupt: #KeyboardInterrupt Detection
        print("[" + str(datetime.datetime.now()) + "] " + "Keyboard Interupted at Sequence number: " + str(seqnum))
        exit()

    except: #If Misc error happened
        print("[" + str(datetime.datetime.now()) + "] " + "Error Occured on sequence number: " + str(seqnum) )
        time.sleep(errorDelay)
        continue
