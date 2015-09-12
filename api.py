#!/usr/bin/python
#coding:utf8
import json
import urllib2
import ConfigParser

class variables():
    def __init__(self):
        '''define zabbix need information'''
        config = ConfigParser.ConfigParser()
        config.read('zabbix.conf')
        if config.has_option("zserver","Url"):
            _url = config.get("zserver","Url")
        if config.has_option("zserver","User"):
            _user = config.get("zserver","User")
        if config.has_option("zserver","Password"):
            _password = config.get("zserver","Password")
        self.url = _url
        self.user = _user
        self.password = _password
        self.header = {"Content-Type": "application/json"}
    def loginData(self):
        data = json.dumps({
			"jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.password
                      },
            "id": 0
          })
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(request)
        except Exception as e:
            print "Auth Failed, Please Check Your Name And Password:",e.code
        else:
            response = json.loads(result.read())
            result.close()
            authID = response['result']
            return authID
    def dataGet(self,data,hostip=""):
        request = urllib2.Request(self.url,data,self.header)
        try:
            result = urllib2.urlopen(request)
        except Exception as e:
            if hasattr(e, "reason"):
                print "Failed to reach a server."
                print "Reason:", e.reason
            elif hasattr(e, "reason"):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
            return 0
        else:
            response = json.loads(result.read())
            result.close()
            return response
    
def main():
    API = variables()
    return API.loginData()
if __name__ == "__main__":
    main()
