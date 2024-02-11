from datetime import datetime, timedelta
import rsa
import os
from glob import glob
from zipfile import ZipFile


period = 30             # days
clientName = input('Please Type Client name: ')
licenseFileName = 'License.lic'
publicKey =rsa.PublicKey(10871363084898070022303896002903391265444392016308981589701418203435182379057843234360336520869928895398932205768274281413654263140154242008097101032149633, 65537)
timeNow = datetime.now()
end_date = timeNow + timedelta(days=period)
fileName = clientName + '_' + str(period) + '.zip'

message = str(end_date)
# publicKey, privateKey = rsa.newkeys(512)
encMessage = rsa.encrypt(message.encode('utf-8'), publicKey)
# wMessage = str(encMessage)

for filePath in glob('*.zip'):
    if os.path.isfile(filePath):
        os.remove(filePath)

with open(licenseFileName, 'wb') as f:
        f.write(encMessage)

zf = ZipFile(fileName, 'w')
zf.write(licenseFileName)
zf.close()

# os.remove(licenseFileName)
