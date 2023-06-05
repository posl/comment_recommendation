def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    i = 0
    sum = 0
    while i < n:
        if i % 2 == 1:
            sum += a[i] - 1
        else:
            sum += a[i]
        i += 1
    if sum <= x:
        print('Yes')
    else:
        print('No')
