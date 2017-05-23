# 在linux和windows上打印彩色文字

## 安装
```
pip install bashcolor
python -m bashcolor
# 如果打印出所有支持的颜色 表示安装成功
```

## 使用
```
from bashcolor import *

COLORS      # 支持的所有颜色
BGCOLORS    # 支持的背景颜色
STYLES      # windows不支持此项

color.red('This is red text')
color.green('This is green text')
```

## color类

    color所支持的颜色 可以调用dir(color)获取到
    color.red(msg, bgcolor, style)
    msg: 自定义的文字
    bgcolor: 背景颜色 可以传入BGCOLOR字典中的所有值
    style: Linux可以传入STYLES字典中的所有值 Windows将忽略它

    每个颜色 还有对应的light开头的方法 这个会高亮显示这个颜色