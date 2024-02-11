from datetime import datetime, timedelta
import rsa
import os
from glob import glob
from zipfile import ZipFile


clientName = input('Please Type Client name: ')
period = int(input('Please Type the Period in days: '))
licenseFileName = 'License.lic'
publicKey =rsa.PublicKey(10871363084898070022303896002903391265444392016308981589701418203435182379057843234360336520869928895398932205768274281413654263140154242008097101032149633, 65537)
timeNow = datetime.now()
end_date = timeNow + timedelta(days=period)
fileName = clientName + '_' + str(period) + '.zip'
format_string = '%Y-%m-%d %H:%M:%S'

message = end_date.strftime(format_string)
encMessage = rsa.encrypt(message.encode(), publicKey)

for filePath in glob('*.zip'):
    if os.path.isfile(filePath):
        os.remove(filePath)

with open(licenseFileName, 'wb') as f:
        f.write(encMessage)

with ZipFile(fileName, 'w') as zf:
    zf.write(licenseFileName)

os.unlink(licenseFileName)
