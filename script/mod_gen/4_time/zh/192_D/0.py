def f(x, m):
    d = int(max(x))
    return len([i for i in range(d+1, m+1) if int(x, d) >= i])
x = input()
m = int(input())
print(f(x, m))
