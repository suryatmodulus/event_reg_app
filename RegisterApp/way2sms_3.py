# python 3
import urllib.request, urllib.error, urllib.parse
import http.cookiejar



def Send_OTP(username,passwd,message,number):

    message = "+".join(message.split(' '))

    #logging into the sms site
    url ='http://site24.way2sms.com/Login1.action?'
    data = 'username='+str(username)+'&password='+str(passwd)+'&Submit=Sign+in'

    #For cookies

    cj= http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    #Adding header details
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        data = data.encode('utf-8')
        usock =opener.open(url, data)
    except IOError:
        print("error")
        #return()

    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(number)+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        send_sms_data = send_sms_data.encode('utf-8')
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print("error")
        #return()

    print("success") 
        #return ()
