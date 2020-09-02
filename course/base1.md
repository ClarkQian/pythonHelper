# 关于开头的部分
## 1. \# -*- coding:utf-8 -*-
>> 为了告诉解释器用utf-8解释我们写的代码  
>> python2默认ascii / python3 默认unicode
## 2. decode and encode
    python3 default is unicode(1:E 2:C attention:utf-8 is 1:E 3:C)
    ![detail](https://img.jbzj.com/file_images/article/202002/202029125042600.png)     
    
    > 1. 为什么读取指令的时候报出的gbk编码错误无法通过改变编码解决: 首先字节对的数目不同无法正确的读取(2个一个汉字和3个一个汉字)，所以我们必须在io流中指定读取的编码
    ```python
        fileIo.buffer().decode(encoding=utf-8)
        # the first step: tell how to read
        # the sencod step: how to transfer
    ```
    > 2. 我们在python中创建的对象是可以utf-8和gbk相互转化的，只需要以unicode作为中介就可以解决，但是必须是我们在python中创建的对象，从外部引入的对象的编码是直接无法读取的，更不谈转化了。 但是比特是可行的话，是可以比特读取再转成对应的汉字编码的
## 3. 关于局部和全局变量
1. 函数内部的是局部变量
2. 我们可以声明 global a(注意不能直接赋值)但是可以后面使用这个引用变量

## 4. 关于生成器和直接列表
1. 生成器使用()
2. 列表使用[]   

## 5. 关于yield
1. 每次运行到这里就会出去，等到下一个Next()的唤醒
2. 可以用 a = yield来控制程序的中断， 其中的只可以用generator.send(value)来实现（取代了next()的功能，不需要再次next()了<next只唤醒不会传值>）
3. 可以用一个 a = yield作为接收线程，然后实用一个生产者使用send进行唤醒，实现单线程的异步效果
