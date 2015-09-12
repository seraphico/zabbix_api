#!/usr/bin/python
#coding:utf8
import json
import api
class itemsMethod():
    def __init__(self):
        self.Variables = api.variables()
        self.loginAuth = api.main()
    def getItems(self):
        data = json.dumps({
			"jsonrpc": "2.0",
			"method": "item.get",
			"params": {
				"output": "extend",
				"sortfield": "name"
    		},
			"auth": self.loginAuth,
			"id": 60
		})
        re = self.Variables.dataGet(data)
        for items in  re['result']:
            print "itemsid: %s itemsname: %s templateid: %s" %(items['itemid'],items['name'],items['templateid'])
