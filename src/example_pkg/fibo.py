# Fibonacci numbers module
# https://docs.python.org/dev/tutorial/modules.html#packages

def fib(n):
    """Write Fibonacci series up to n
    
        Parameters
        ----------
        n : int
            Positive integer
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n
    
        Parameters
        ----------
        n : int
            Positive integer
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
