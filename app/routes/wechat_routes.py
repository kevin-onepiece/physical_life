from flask import Blueprint, request, make_response
import xml.etree.ElementTree as ET
import time
from app.services.wechat_service import handle_user_input

wechat_bp = Blueprint('wechat', __name__)

WECHAT_TOKEN = 'foo'

@wechat_bp.route('/wechat', methods=['GET'])
def wechat_check():
    from hashlib import sha1
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    check_list = [WECHAT_TOKEN, timestamp, nonce]
    check_list.sort()
    s = ''.join(check_list)
    if sha1(s.encode('utf-8')).hexdigest() == signature:
        return echostr
    else:
        return "fail"

@wechat_bp.route('/wechat', methods=['POST'])
def wechat_response():
    xml_data = request.data
    xml = ET.fromstring(xml_data)

    to_user = xml.find("ToUserName").text
    from_user = xml.find("FromUserName").text
    content = xml.find("Content").text
    msg_type = xml.find("MsgType").text

    if msg_type == 'text':
        reply_content = handle_user_input(content, to_user, from_user)
        response = f"""
        <xml>
            <ToUserName><![CDATA[{from_user}]]></ToUserName>
            <FromUserName><![CDATA[{to_user}]]></FromUserName>
            <CreateTime>{int(time.time())}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{reply_content}]]></Content>
        </xml>
        """
        return make_response(response)
    else:
        return "success"