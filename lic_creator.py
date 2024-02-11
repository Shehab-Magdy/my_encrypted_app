from datetime import datetime, timedelta
import rsa
import os
import glob
import zipfile
 

period = 30             # days
clientName = input('Please Type Client name: ')
fileName = clientName + '_' + str(period) + '.zip'

timeNow  = datetime.now()
end_date = timeNow + timedelta(days=period)

message = str(end_date)

publicKey, privateKey = rsa.newkeys(512)
encMessage = rsa.encrypt(message.encode(), publicKey)

wMessage = str(encMessage)


for filePath in glob.glob('*.zip'):
    if os.path.isfile(filePath):
        os.remove(filePath)

f = open('License.lic', "w")
f.write(wMessage)
f.close()

zf = zipfile.ZipFile(fileName,'w')
zf.write('License.lic')
zf.close()

os.remove('License.lic')
