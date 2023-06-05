def replace(n):
    n = str(n)
    n = n.replace('1','x')
    n = n.replace('9','1')
    n = n.replace('x','9')
    return int(n)
n = int(input())
print(replace(n))
