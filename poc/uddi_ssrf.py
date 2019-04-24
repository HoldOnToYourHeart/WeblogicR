#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
imrport sys
imrport requests

headers = {'user-agent': 'ceshi/0.0.1'}

def islive(rip,rport):
    rip='http://' + str(rip)+':'+str(rport)+'/uddiexplorer/'
    r = requests.get(rip, headers=headers)
    # print(rip,r.status_code)
    return r.status_code

def run(rip,rport):
    if islive(rip,rport)==200:
        print(u'[+]目标weblogic存在UDDI组件!\n[+]路径为:{}\n[+]请自行验证SSRF漏洞!'.format('http://' + str(rip)+':'+str(rport)+'/uddiexplorer/'))
    else:
        print(u"[-]目标weblogic UDDI组件默认路径不存在!")

if __name__=="__main__":
    #rip = sys.argv[1]
    #rport = int(sys.argv[2])
    run(rip,rport)
