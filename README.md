# aconfig
python 加载可用配置项
## 使用举例
### 修饰方法
``` Python
from bllose.config.Config import bConfig

@bConfig()
def my_function_need_config(*args, config):
    myValue = config('myKey')
```

### 修饰类
``` Python
from bllose.config.Config import class_config

@class_config
class myClass():
    def __init__(self, config):
        myValue = config('myKey')
```
