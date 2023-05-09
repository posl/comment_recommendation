def solve():
    n,m,t = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    ab.sort()
    battery = n
    prev = 0
    for i in range(m):
        battery -= ab[i][0] - prev
        if battery <= 0:
            print("No")
            return
        battery += ab[i][1] - ab[i][0]
        if battery > n:
            battery = n
        prev = ab[i][1]
    battery -= t - prev
    if battery <= 0:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    solve()