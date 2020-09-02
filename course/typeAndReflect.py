
## 1. 类的祖先type
我们可以通过type()创建类
```python
    def show(self):
    print("this is show function")


    classTest = type("classTest",(),{'talk':show})
    # now the classTest is the same as class classTest
    print(type(classTest))
    test = classTest()
    test.talk()

```
## 2. 反射
- realizing memory loading and detaching dynamiclly
1. hasattr(object, attr) -> return attr 
2. getattr(object, attr)
3. create a reflect(object(x) add func (y)/attr to a object, add content(v)):  
which is equivalient to  x.y = v
    ```python
    setattr(object, function_name, func/attr_address)

    setattr(object, attr_name, attr_value)

    func(self) # mimic the class function

    #execute
    object.func(object) # have to pass itself as self obejct
    ```
4. delattr(object, attr)
>- attention:  
    although setattr add a reflect in the object, but there is still no function is the name of the object.  
    for instance, you will find obj.function_name() will not work, but you can use func = getattr(object, func_name) to get the function or object which will work very well (you can understand it like that they are not in the same filed may be look like in the reflect owned filed to restore the attributes)
