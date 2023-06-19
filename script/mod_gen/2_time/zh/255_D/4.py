def problem255_d():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for i in range(q)]
    sum = 0
    for i in range(1,n):
        sum += abs(a[i]-a[i-1])
    for i in range(q):
        if x[i] == 0:
            print(sum)
        else:
            if x[i] == a[0]:
                sum += abs(a[1]-a[0])
                sum -= abs(a[1]-a[0]-1)
            elif x[i] == a[n-1]:
                sum += abs(a[n-1]-a[n-2])
                sum -= abs(a[n-1]-a[n-2]-1)
            else:
                sum += abs(a[1]-a[0])
                sum += abs(a[n-1]-a[n-2])
                sum -= abs(a[1]-a[0]-1)
                sum -= abs(a[n-1]-a[n-2]-1)
            a[0] = x[i]
            a[n-1] = x[i]
            print(sum)

if __name__ == '__main__':
    problem255_d()