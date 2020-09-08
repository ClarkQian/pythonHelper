# multiprocess

## 1. main starting

- start(the same as thread)

  ```python
  def run():
      pass
  multiprocessing.Process(target= run, args=("",)).start()
  ```

  

  

- get process id

  ```python
  os.getppid() # parent's id
  os.getpid() # get my own id
  ```

## 2. share data between processes

#### 1. transmit data

- using threading Queue: useful but not convinient

  ```python
  from multiprocess import Process, Queue
  # the same grammer with threading ones 
  # ☣ different processes will not share the context, so you must pass the queue by param instead of using it as a context variable like threading did before.
  # different processes share the data by pickle
  ```

- using pipes

  ```python
  parent_conn, child_conn = Pipe()
  parent = Process(target=f, args=(child_conn,))
  child = Process(targe=f, args=(parent_conn,))
  conn.send(data)
  conn.recv() # no data will block 
  
  ```

  

#### 2. share data

- using manager

  ```python
  manager = Manager() # you can use different type of data structure
  dict = manager.dict() #create a share dictionary
  val  manager.Value(int, 0)#(typecode, value)
  list = manager.list(range(5)) # creating a share list
  
  ```

  

#### 3. lock

- using Lock()

  > make sure that the screen is be used by only one process

#### 4. process pool

```python
from multiProcess import Pool

# must in windows
if __name__ == '__main__': #if this file is executed __name__ will be __mian__
#other .py will make __name__ to be the module name, ofen as file name

    pool = Pool(5)
    ## apply way is serial
    pool.apply(func=Foo, args(i,))
    pool.apply(func=Foo, args(i,))
    pool.close() # is a problem close first
    pool.join()# escape the main process end immediately
	
    ## apply_async is parallel
    pool.apply_async(func=Foo, args=(i,) callback= func2)# call back is the ending process of finishing the process, executed by main process
    
    ## call back function must have a argument

```

