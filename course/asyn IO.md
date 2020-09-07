## asychronous IO

### 1. 协程(Coroutine)

- 用户态轻量级线程，本质是个单线程

- 遇到Io操作就切换线程（IO操作不需要CPU参与）

#### greenlet：启动携程

```python
#switch by hands
gr1 = greenlet(run1)
gr2 = greenlet(runt2)
gr1.switch()

#in run1
#using gr2.switch() to switch to other coroutines


# switch autoly
#starting
gevent.joinall([
    gevent.spawn(foo，args),
    gevent.spawn(bar)
])

gvent.spawn(func, args)

#in cuntion 遇到阻塞会自动切换任务 #必须要适配对应的io操作，要告诉gevent是Io操作
gevent.sleep(n)#sleep second, when encouter it swith automatically
#告诉gevent所有io操作工作
import from gevent import monkey
monkey.patch_all() # 把所有Io都打上补丁

```

#### 论事件驱动与异步IO

- 事件驱动的模型（类比鼠标点击的方式）

  > 使用事件（消息）队列

#### blocking I/O

- 无法在单线程下实现多个socket连接

#### Nonblocking I/O

- 不停地询问，发现Kernel没有准备好，就raise error， 然后继续做事儿
- 可以实现用户看到的socket多路并发

#### IO多路复用

- select 传送了100多个socket句柄，只要有其中的一个数据准备好了，select就会返回

#### 🚢异步I/O

- read发送一个请求，之后立刻返回
- kernel收到了一个请求，之后立刻返回 
- kernel在完成了copy到用户内存之后通知read操作完成

#### 小结

![关系图](https://images2015.cnblogs.com/blog/720333/201609/720333-20160916171648430-240094129.png)

### code about

1. 多路复用

   一个发送一个打包的read错做，然后其中有一个准备好了，就会通知read,然后read自己从内存里面取

   - select

   - poll

   - epoll

```python
#select
#todo: add it later
```

