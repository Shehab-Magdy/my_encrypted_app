from datetime import datetime
import rsa
from urllib.request import urlopen

privateKey = rsa.PrivateKey(10871363084898070022303896002903391265444392016308981589701418203435182379057843234360336520869928895398932205768274281413654263140154242008097101032149633, 65537,
                            385508152788548678331846961422516766115213803590369916451258005474516133367698561857908095342705954167887778857671955182026522553679602393048233993306049, 7061775828138545816307681607909344123743672579355147260993004442982248117897357637, 1539465900571317804571833622904443816187391593971375228443576129770205709)
licenseFileName = 'License.lic'
format_string = '%Y-%m-%d %H:%M:%S'

with open(licenseFileName, 'rb') as f:
    for encMessage in f:
        decMessage = rsa.decrypt(encMessage, privateKey).decode()

expiryDate = datetime.strptime(decMessage, format_string)
def get_current_date():
    url_content = urlopen('http://just-the-time.appspot.com/')
    current_date = url_content.read().strip()
    current_date = current_date.decode('utf-8')
    current_date = datetime.strptime(current_date, format_string)
    return current_date

if get_current_date() > expiryDate:
    print('This application is expired, Please contact your vendor.')
