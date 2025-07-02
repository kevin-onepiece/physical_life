from xpyunopensdk.service import xpyunservice
from xpyunopensdk.model import model
from xpyunopensdk.util import xputil
import time

# 构造请求对象-公共参数
user_name = "kevinfu2048@foxmail.com"
user_key = "e96c5cebfb0f4de69035f03c726be762"
current_time = int(time.time())
sn = "25GTGERACTE1448"

# 添加打印机
def add_printer():
    request = model.AddPrinterRequest(user_name, user_key)
    request.sign = xputil.sign(user_name + user_key + str(current_time))  # 按API文档生成
    request.debug = True
    # 获取当前时间戳
    request.timestamp = current_time  # 当前时间戳
    # 通常还需要调用 request.generateSign() 方法自动生成 sign
    # 构造打印机 item
    printer_item = model.AddPrinterRequestItem()
    printer_item.sn = sn
    printer_item.name = "打印机"
    request.items = [printer_item]
    # 调用批量添加打印机接口
    result = xpyunservice.xpYunAddPrinters(request)
    print(result)

def do_print():
    request = model.PrintRequest(user_name, user_key)
    request.sign = xputil.sign(user_name + user_key + str(current_time))  # 按API文档生成
    request.debug = True
    request.timestamp = current_time
    request.content = "实物人生-下班打印"
    request.sn = sn
    xpyunservice.xpYunPrint(request)

if __name__ == '__main__':
    # add_printer()
    do_print()
