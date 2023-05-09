def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(0,n):
        if i%2 == 0:
            sum += a[i]
        else:
            sum += a[i] - 1
    if sum <= x:
        print("Yes")
    else:
        print("No")
