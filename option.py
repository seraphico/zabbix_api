#!/usr/bin/python
#coding:utf8
import argparse

def main():
    parser = argparse.ArgumentParser(description="This is api script module.")
    parser.add_argument('-H','--hostname',dest='hostname', type=str,default='Zabbix example host',
								help='Specify zabbix hostname.(--Defalut:Zabbix example host)')
    
    parser.add_argument('-I','--ipaddress',dest='ip', type=str,default='127.0.0.1',
								help='Specify zabbix ipaddress.(--Default:127.0.0.1)')
    
    parser.add_argument('-i','--hostid',dest='hostid', type=str,default='null',
								help='Specify zabbix hostid.(--Default:0)')
    
    parser.add_argument('-G','--groupname',dest='groupname', type=str,default='Zabbix_API',
								help='Specify zabbix groupname.(--Default:Zabbix_API)')
    
    parser.add_argument('-g','--groupid',dest='groupid', type=str,default='93',
								help='Specify zabbix groupid(--Default:93)')
    
    parser.add_argument('-T', '--templatename',dest='templatename', type=str,default='Template OS Linux',
								help='Specify template name.(--Default:Template OS Linux)')
    
    parser.add_argument('-t','--templateid',dest='templateid', type=str,default='10382',
								help='Specify templateid.(--Default:10382)')
    
    parser.add_argument('-M','--method',dest='hostmethod', type=str,default='gethostdata',
								help='Specify operate method.(--Default:gethostdata)')
    parser.add_argument('-e','--exist',dest='exist', type=str,default='HOST Group',
								help='Specify operate method.(--Default:HOST Group)')
    return parser
