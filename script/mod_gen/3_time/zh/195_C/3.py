def f(n):
    if n<1000:
        return 0
    else:
        return 1+f(n//1000)
n = int(input())
print(sum([f(i) for i in range(1,n+1)]))
