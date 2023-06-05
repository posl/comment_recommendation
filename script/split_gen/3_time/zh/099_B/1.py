def getSnowDepth(a,b):
    """
    根据题目中的条件，可以得出如下公式：
    a = x + (x+1) + (x+2) + ... + (x+n)
    b = (x+1) + (x+2) + ... + (x+n) + (x+n+1)
    化简得：
    a = nx + n(n+1)/2
    b = (n+1)(n+2)/2 + nx
    化简得：
    b = 2a + n + 1
    n = b - 2a - 1
    """
    n = b - 2*a - 1
    return n
