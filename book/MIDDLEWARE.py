


def MIDDLEWARE(func):
    def wapper(*args,**kwargs):
        print("使用了中间件 -全局装饰器")
        re = func(*args,**kwargs)
        print("使用了中间件 -全局装饰器1")

        return re
    return wapper