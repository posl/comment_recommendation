def fun(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            for j in range(1,n+1):
                if j % 2 == 1:
                    count += 1
    return count
print(fun(3))
print(fun(6))
print(fun(11))
print(fun(50))
