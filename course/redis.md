# redis

## 连接

```python
import redis

r = redis.Redis(host='localhost',port=6379)

r.set('name','Mike')
print(r.get('name').decode())
r.close()
```



## string

```python
r.set()
r.get()#还可以添加延时删除，详情参考文档
#hash set add it later
```

