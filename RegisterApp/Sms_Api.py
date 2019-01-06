import requests

def Send_Sms(number,message):
    url = "https://control.msg91.com/api/sendhttp.php?authkey=144888A5cM4rfEm5d58c7d224&sender=FURORE&route=4&country=91"
    payload={'mobiles':number,'message' : message}
    r = requests.post(url, data=payload)
    print(r.text)
