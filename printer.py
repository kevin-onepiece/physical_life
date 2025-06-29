from xpyunopensdk.service import xpyunservice
from xpyunopensdk.model import model as model

# 构造打印机 item
printer_item = model.PrinterItem(sn="C58HHWL46250006", name="打印机")
# 构造请求对象
request = model.AddPrinterRequest(
    user="kevinfu2048@foxmail.com",
    userKey="9eb5e43619fa4f5796a31e4667371f15",
    sign="签名",
    debug=False,
    timestamp=1234567890,
    items=[printer_item]
)

# 调用批量添加打印机接口
result = xpyunservice.xpYunAddPrinters(request)
print(result)