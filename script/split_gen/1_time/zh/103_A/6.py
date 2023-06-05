def solve():
    #这里写你的代码
    a = list(map(int, input().split()))
    a.sort()
    print(a[2]-a[0])
