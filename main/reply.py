'''
Created on Oct 13, 2016

@author: xhuiton
'''
import time

class Msg(object):
    def __init__(self):
        pass
    def send(self):
        return "success"
    
class TextMsg(Msg):
    def __init__(self,toUserName,fromUserName,content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
        
    def send(self):
        Xml = '<xml><ToUserName><![CDATA['+self.__dict['ToUserName']+']]></ToUserName><FromUserName><![CDATA['+self.__dict['FromUserName']+']]></FromUserName><CreateTime>'+str(self.__dict['CreateTime'])+'</CreateTime><MsgType><![CDATA[{text}]]></MsgType><Content><![CDATA['+self.__dict['Content']+']]></Content></xml>'
#	print '==============='+Xml  
#	xml = 'iiiiiiiiiiii'      
#	print xml
        return Xml

        
        
class ImageMsg(Msg):
    def __init__(self,toUserName,fromUserName,mediaID):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = mediaID
        
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[{image}]]></MsgType>
        <Image><MediaId><![CDATA[{MediaId}]]></MediaId></Image>
        </xml>
        """
        
        return XmlForm.format(**self.__dict)

















    
