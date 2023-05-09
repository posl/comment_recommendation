def check():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum >= sum(a) / (4*m):
        print("Yes")
    else:
        print("No")
check()

if __name__ == '__main__':
    check()