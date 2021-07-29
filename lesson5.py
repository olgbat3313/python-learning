#def decorator_func(func):
 #   def wrapper():
  #      print('start')
   #     func()
    #    print('end')
    #return wrapper

#@decorator_func
#def hello():
 #   print('hello')
#print(hello())


def decorator_func(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        print('start')
       # import pdb; pdb.set_trace()
        if args[0].isdigit():
            raise ValueError('Name must be a string')
            
        func(*args, **kwargs)
        print('end')
        end = time.time()
        print(f'Time of work {end - start}')
    return wrapper

@decorator_func
def hello(name):
    print(f'hello, {name}')
hello('12jh3')


import time
functions_requests = {
    'funcA':0,
    'funcB':0,
}


functions_time = {
    'funcA':0,
    'funcB':0,
}


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        functions_requests[args[0]] +=1
        functions_requests[args[0]] += (end-start)
    return wrapper

@benchmark
def funcA(func_name='funcA'):
    ...


@benchmark
def funcB(func_name='funcB'):
    ...

funcA('funcA')
funcB('funcB')
    