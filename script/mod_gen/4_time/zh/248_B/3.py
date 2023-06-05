def f(a,b,k):
    count = 0
    while a < b:
        a *= k
        count += 1
    return count
a,b,k = map(int,input().split())
print(f(a,b,k))
