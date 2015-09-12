#!/usr/bin/python
#coding:utf8
import sys
import host
import option
import hostgroup

Parse = option.main().parse_args()
if Parse.hostmethod == "getHost":
    Instancehost = host.hostMethod().gethostData()
    for hostinfo in  Instancehost:
        print "HostId: %s hostName: %s"%(hostinfo['hostid'],hostinfo['host'])
elif Parse.hostmethod == "hostAdd":
    Instancehost = host.hostMethod().createhostData(hostname=Parse.hostname,hostip=Parse.ip,tempid=Parse.templateid,groupid=Parse.groupid)
    print Instancehost   
elif Parse.hostmethod == "groupAdd":
    Instancegroup = hostgroup.groupMethod().createGroup(hostg=Parse.groupname)
    print Instancegroup
elif Parse.hostmethod == "groupDel":
    InstanceDelgroup = hostgroup.groupMethod().deleteGroup(groupid=Parse.groupid)
    print InstanceDelgroup
elif Parse.hostmethod == "getGroup":
    InstanceGetgroup = hostgroup.groupMethod().getgroupData()
    print InstanceGetgroup
elif Parse.hostmethod == "ghexist":
    InstanceExisgroup = hostgroup.groupMethod().existGroup(groupg=Parse.groupname)
    if InstanceExisgroup:
        print "Host group is exist."
    else:
        print "Host group is not exist."

else:
    print Parse.help
    sys.exit[1]
