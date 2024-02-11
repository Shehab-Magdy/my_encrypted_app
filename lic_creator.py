from datetime import datetime, timedelta
import rsa
 

period = 30             # days
timeNow  = datetime.now()
end_date = timeNow + timedelta(days=period)

message = str(end_date)

publicKey, privateKey = rsa.newkeys(512)
encMessage = rsa.encrypt(message.encode(), publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

