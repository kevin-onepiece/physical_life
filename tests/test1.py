import time
from xpyunopensdk.util import xputil

print(int(time.time()))


user_name = "kevinfu2048@foxmail.com"
user_key = "9eb5e43619fa4f5796a31e4667371f15"
sign = xputil.sign(user_name + user_key + str(time.time()))  # 按API文档生成

print(sign)

print(xputil.getSeconds())
print(int(time.time()))