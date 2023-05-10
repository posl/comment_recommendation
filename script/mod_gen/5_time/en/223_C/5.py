def solve():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i],b[i] = map(int,input().split())
    total = 0
    for i in range(n):
        total += a[i]/b[i]
    half = total/2
    time = 0
    for i in range(n):
        time += a[i]/b[i]
        if time >= half:
            print(time - (time - half)*2)
            break

if __name__ == '__main__':
    solve()