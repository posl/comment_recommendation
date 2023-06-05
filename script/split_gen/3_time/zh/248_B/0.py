def cal(a,b,k):
    count = 0
    while a < b:
        a = a * k
        count += 1
    return count
a,b,k = map(int,input().split())
print(cal(a,b,k))
