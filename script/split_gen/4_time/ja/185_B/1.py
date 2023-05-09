def solve():
    #n, m, t = map(int, input().split())
    #ab = [list(map(int, input().split())) for _ in range(m)]
    n, m, t = 10, 2, 20
    ab = [[9, 11], [13, 17]]
    #n, m, t = 10, 2, 20
    #ab = [[9, 11], [13, 16]]
    #n, m, t = 15, 3, 30
    #ab = [[5, 8], [15, 17], [24, 27]]
    #n, m, t = 20, 1, 30
    #ab = [[20, 29]]
    #n, m, t = 20, 1, 30
    #ab = [[1, 10]]
    #print(n, m, t)
    #print(ab)
    battery = n
    current = 0
    for i in range(m):
        #print("battery", battery)
        #print("current", current)
        #print("ab[i][0]", ab[i][0])
        #print("ab[i][1]", ab[i][1])
        battery -= (ab[i][0] - current)
        if battery <= 0:
            print("No")
            return
        battery += (ab[i][1] - ab[i][0])
        if battery > n:
            battery = n
        current = ab[i][1]
    battery -= (t - current)
    if battery <= 0:
        print("No")
        return
    print("Yes")
