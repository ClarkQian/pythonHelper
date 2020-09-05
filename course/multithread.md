# thread about

 ## 1. theory

- thread:  is an execution `context`, which is all the information a CPU needs to execute a stream of instructions. A CPU is giving you the illusion that it's doing multiple computations at the same time.

  > many threads can share a cpu core without worrying  about working not well.

- process:  an executing instance of a program is called a process.

  > a process can have one or many threads  
  >
  > a process is created by a primary thread,  but can create additional threads from any of its threads.
  >
  > all the threads in a process have the `same` view of the memory and communicate with each other.
  >
  > different processes do not share memory and can not communicate directly only can realize it by `interprocess`.
  >
  > thread can control other threads but only father process can control child processes.

## 2. code about

### 1. working by function  

-  threading.Thread(target=func, args=("51",))  special grammar

> ⚠ args=("",)传入的是51 ，而 args="12"传入的是a = 1 b = 2

### 2. working by class

1. MyClass(threading.Thread) by inherienting

2. override init

3. create run function

```python
class MyThread(threading.Thread):
    def __inti__(self, n):
        super(MyThread, self).__init__()
        self.n = n
    def run(self):
        print(self.n)
        
```

4. run by

   > myThreadObj.start() # auto running run function()

> ⚠ main thread is independent with other threads
>
> but how to make main thread stop just before exe ends?
>
> using `threadn.join()` # waiting threadn to finish and then go on this thread. 
>
> `join()`will be used to suspend current thread to make threadn finished.
>
> the thinking is that start all the thread and save all the thread in a list, and  n.join() all the thread, so the main thread will always wait for all the subthread finishing and then continue.

> tips: you can use `threading.current_thread()` to get the current thread name.

### 3.  daemon thread

- daemon thread means the king die and the sam e time all the sub threads die immediately

1. how to create

   ```python
    t.setDaemon(True)
    t.start()
   ```

   

### 4. lock

- thread lock

  ```
  lock = threading.Lock() #getting a global lock
  
  
  execution():
  	lock.acquire()
  	# execuation()
  	lock.release()
  ```

  

- recursive lock

  ```python
  lock = threading.Lock()
  # solve the problem of recursive function: inner function would like to use the father's key
  ```

  

- Semaphore(信号量)

  it works like several pairs of keys

  ```python
  semaphore = threading.BoundedSemaphore(5) #5 locks in maximum
  
  semaphore.acquire()
  execation
  semaphore.release()
  ```

  

### 5. Events

An event is a simple synchronization object.

> red light mode:
>
> while True:
>
> ​	if counter > 30:
>
> ​		redLight = True
>
> ​	if counter > 50:
>
> ​		redLight = False
>
> ​		counter  =  0
>
> 

1.  create event

   > event = threading. Event()

2. using it 

   ```python
   # a red light tower
   event  threading.Event()
   event.clear() #把标志位清了
   event.set() #设置标志位
   用这个构造一个全局的标志，参考成有一个所有人都可以看见的红绿灯
   
   # cars
   if event.is_set():
       pass
   else:
       event.wait() # waiting for the next led(flag) is set< waiting event.set()>
   
   
   ```

   

### 6. queue

- queue.Queue()

```python
q = queue.Queue()#maxsize=n if reach maxsize, there will be a block
queue.put()
queue.get()#block = False: the same function as below
queue.get_nowait() # without wait and raise exception
queue.qsize()

```

- queue.LifoQueue()

  ```python
  last in first out
  
  ```

  

- queue.PriorityQueue() 

  ```python
  queue.PriorityQueue()
  queue.put((1,obj))
  queue.put((2,obj))
  queue.put((3,obj))
  ```

  

  
