#!/usr/bin/python
#coding:utf8
import json
import api
class templateMethod():
    def __init__(self):
        self.loginAuth = api.main()
        self.Variables = api.variables()
    def getemplateData(self):
        data = json.dumps({
			"jsonrpc": "2.0",
			"method": "template.get",
			"params": {
				"output": "extend"
        		},
    		"auth": self.loginAuth,
    		"id": 50
		})
        re = self.Variables.dataGet(data)
        for templates in re['result']:
            print "TemplateID: %s TemplateName: %s " %(templates['templateid'],templates['name'])

templateAPI = templateMethod()
print templateAPI.getemplateData()
