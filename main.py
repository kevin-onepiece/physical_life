from flask import Flask, request, make_response
import xml.etree.ElementTree as ET
import time

app = Flask(__name__)

# 你的服务器验证用的 token（在微信公众平台中设置）
WECHAT_TOKEN = 'your_token_here'

# 微信接入验证（GET 请求）
@app.route('/wechat', methods=['GET'])
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

# 接收微信消息（POST 请求）
@app.route('/wechat', methods=['POST'])
def wechat_response():
    xml_data = request.data
    xml = ET.fromstring(xml_data)

    # 解析用户消息
    to_user = xml.find("ToUserName").text
    from_user = xml.find("FromUserName").text
    content = xml.find("Content").text
    msg_type = xml.find("MsgType").text

    print(content)

    # 响应文本消息
    if msg_type == 'text':
        reply_content = handle_user_input(content)

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

# 处理文本内容逻辑：你可以在这里写分类逻辑
def handle_user_input(content):
    if "买了" in content or "花了" in content:
        
        return "已记录账单 ✅"
    elif "提醒" in content or "待办" in content:
        return "待办事项已添加 📌"
    else:
        return "暂未识别，可输入 #记账 或 #待办 开头内容"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
