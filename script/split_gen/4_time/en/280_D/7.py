def fact(n): 
    if n == 0: 
        return 1
    return n * fact(n-1) 
k = int(input())
n = 1
while True:
    if fact(n) % k == 0:
        print(n)
        break
    else:
        n += 1
