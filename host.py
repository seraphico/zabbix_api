#!/usr/bin/python
#coding:utf8
import json
import api
import urllib2
import option

class hostMethod():
    def __init__(self):
        self.Variables = api.variables()
        self.loginAuth = api.main()
    def gethostData(self,hostip=""):
        data = json.dumps({
			"jsonrpc": "2.0",
			"method": "host.get",
			"params": {
				"output": "extend",
				"filter": {
					"host":[]
				}
    		},
			"auth": self.loginAuth,
			"id": 1
     	})
        re = self.Variables.dataGet(data)
        return re['result']
    def createhostData(self, tempid="10382", groupid="93",hostname="",hostip=""):
        data = json.dumps({
			"jsonrpc": "2.0",
    		"method": "host.create",
    		"params": {
        		"host": hostname,
        		"interfaces": [
            		{
                		"type": 1,
                		"main": 1,
                		"useip": 1,
                		"ip": hostip,
                		"dns": "",
                		"port": "10050"
            		}
        		],
				"groups": [{"groupid": groupid }],
				"templates": [{"templateid": tempid}],
            },
 			"auth": self.loginAuth,
			"id": 1
		})
        re = self.Variables.dataGet(data)
        return re['result']

