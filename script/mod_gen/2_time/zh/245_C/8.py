def check(a,b,k):
    # a,b,k = map(int, input().split())
    a = list(map(int, a.split()))
    b = list(map(int, b.split()))
    for i in range(len(a)):
        if abs(a[i]-b[i])>k:
            return "No"
    return "Yes"
a = "1 1 1000000000 1000000000"
b = "1 1000000000 1 1000000000"
k = 1000000000
print(check(a,b,k))
