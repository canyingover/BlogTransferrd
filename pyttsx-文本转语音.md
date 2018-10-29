---
title: pyttsx 文本转语音
date: 2017-03-12 18:43:28
categories: Python
---

感觉挺有趣，不是很难，权当记录一下简单的实现方式，其他API实现可参考[doc](http://pyttsx.readthedocs.io/en/latest/drivers.html)：

<!-- more -->
``` python
import pyttsx

engine = pyttsx.init()
# set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0])
# set rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+30)

text = u'中央电视台，中央电视台!'
engine.say(text)

# save to mp3.file
engine.speakToFile(text, r"./123.mp3")
engine.runAndWait()

```

### 设置输出到文件
+ `pyttsx`的官方版本不支持在windows系统下输出到文件，通过下载[github](https://github.com/wojiaohgl/pyttsx)上的修改版本，在将其替代原来安装的版本,可以在`python shell`中,通过`import pyttsx`和`pyttsx`,找到`pyttsx`的位置。
+ 安装comtypes、 win32com,并修改pyttsx里的sapi5.py文件，将`comtypes`的导入语句修改为：
``` python
from comtypes.client import CreateObject
engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
from comtypes.gen import SpeechLib

```

### 参考
+ [http://blog.wojiaohgl.com/archives/267](http://blog.wojiaohgl.com/archives/267)