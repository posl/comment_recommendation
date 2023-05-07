def cal(n, l):
    sum = 0
    for i in range(1,n+1):
        sum += l + i - 1
    return sum
n, l = map(int, input().split())
