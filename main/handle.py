'''
Created on Oct 13, 2016

@author: xhuiton
'''
import web
import hashlib
import receive
import reply
class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello,this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "VipXiaoMiZhou"
            
            list = [token,timestamp,nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode,signature: ", hashcode,signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception,Argument:
            return Argument
        
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ",webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = "test"
                    replyMsg = reply.TextMsg(toUser,fromUser,content)
                    print replyMsg
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
                    print replyMsg
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "do not handle in this moment"
                return reply.Msg().send()
        except Exception,Argment:
            print 'exception'
            return Argment