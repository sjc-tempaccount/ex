import time

def timer1(func):
    """
    Time a function, a decorator
    """
    def wrapper(*arg, **kw):
        ts = time.time()
        result = func(*arg, **kw)
        te = time.time()
        print(f'result:{result} took: {te - ts} sec' )  
        return result
    return wrapper



import functools
def timer2(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print(f'result:{result} took: {te - ts} sec' )          
        return result
    return wrapper

@timer1
def f():
    time.sleep(5)

f()    

