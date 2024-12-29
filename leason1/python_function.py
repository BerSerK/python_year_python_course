# 函数
def greet_user():
    '''
    显示简单的问候语
    '''
    print("Hello!")

# 计算fibonaci数列
def fib(n):
    '''
    计算fibonaci数列
    '''
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)