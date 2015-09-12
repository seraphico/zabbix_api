#!/usr/bin/python
#coding:utf8
import api
import json
class groupMethod():
    def __init__(self):
        self.loginAuth = api.main()
        self.Variables = api.variables()
    def getgroupData(self):
        data = json.dumps({
			"jsonrpc": "2.0",
			"method": "hostgroup.get",
			"params": {
				"output": "extend"
    			},
    		"auth": self.loginAuth,
    		"id": 40
		})
        re = self.Variables.dataGet(data)
        for algroupname in re['result']:
            print   "GroupID:%s GroupName:%s " %(algroupname['groupid'],algroupname['name'])
    def createGroup(self,hostg=""):
        data = json.dumps({
			"jsonrpc": "2.0",
			"method": "hostgroup.create",
			"params": {
				"name": hostg
				},
			"auth": self.loginAuth,
			"id": 41
		})
        re = self.Variables.dataGet(data)
        return re['result']
        
    def deleteGroup(self,groupid=""):
        data = json.dumps({
			"jsonrpc": "2.0",
			"method": "hostgroup.delete",
			"params": [groupid],
			"auth": self.loginAuth,
    		"id": 42
		})
        re = self.Variables.dataGet(data)
        return re['result']
    def existGroup(self,groupg=""):
        data = json.dumps({
			"jsonrpc": "2.0",
            "method": "hostgroup.exists",
			"params": {
				"name": groupg
				},
			"auth": self.loginAuth,
			"id": 43
		})
        re = self.Variables.dataGet(data)
        return re['result']
