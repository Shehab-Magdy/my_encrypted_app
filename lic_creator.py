from datetime import datetime, timedelta
import rsa
import os
import glob
 

period = 30             # days
clientName = input('Please Type Client name: ')
fileName = clientName + '_' + str(period)

timeNow  = datetime.now()
end_date = timeNow + timedelta(days=period)

message = str(end_date)

publicKey, privateKey = rsa.newkeys(512)
encMessage = rsa.encrypt(message.encode(), publicKey)

wMessage = str(encMessage)


for filePath in glob.glob('*.lic'):
    if os.path.isfile(filePath):
        os.remove(filePath)

f = open(fileName, "w")
f.write(wMessage)
f.close()