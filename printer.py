from xpyunopensdk.service import xpyunservice
from xpyunopensdk.model import model
from xpyunopensdk.util import xputil
import time

# 构造请求对象-公共参数
user_name = "kevinfu2048@foxmail.com"
user_key = "e96c5cebfb0f4de69035f03c726be762"
current_time = int(time.time())
sn = "25GTGERACTE1448"

def print_text(content):
    current_time = int(time.time())
    request = model.PrintRequest(user_name, user_key)
    request.sign = xputil.sign(user_name + user_key + str(current_time))
    request.debug = True
    request.timestamp = current_time
    request.content = content
    request.sn = sn
    xpyunservice.xpYunPrint(request)

def generate_todo_list(task_name: str, completed_count: int) -> str:
    return f"""
<C>实物人生</C><BR>
<CB>TO DO LIST</CB><BR>
<BR>
<B><L> {task_name}</L></B><BR>
<BR>
——————————————<BR>
<L> 完成：{completed_count}</L><BR>
<BR><BR>
<C>Level up one habit at a time.</C><BR>
"""

def generate_payment_receipt(total: int, items: list, today_total: int) -> str:
    items_text = "<BR>".join([f"{name}-<CY ct=1></CY> {amount}" for name, amount in items])
    return f"""
<C><N>实物人生</N></C><BR><CB>支付凭证</CB><BR>
<BR>
<B><L>金额：<CY ct=1></CY>  {total}</L></B><BR>
<BR>
<L>{items_text}</L><BR>
<BR>
——————————————<BR>
<L><CY ct=3></CY> 今日消费 <CY ct=3></CY>  <CY ct=1></CY> {today_total}</L><BR>
<BR><BR>
<C>Save first, upgrade later.</C><BR>
"""

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
    print_text("实物人生-下班打印")

def print_todo(content):
    todo_template = f"【待办清单】\n{content}\n----------------"
    print_text(todo_template)

def print_bill(content):
    bill_template = f"【记账】\n{content}\n----------------"
    print_text(bill_template)

if __name__ == '__main__':
    # add_printer()
    do_print()
