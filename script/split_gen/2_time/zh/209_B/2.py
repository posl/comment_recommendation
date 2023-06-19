def main():
    # input
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    # process
    sum = 0
    for i in range(n):
        if i%2 == 1:
            sum += a[i]-1
        else:
            sum += a[i]
    # output
    if sum <= x:
        print("Yes")
    else:
        print("No")
