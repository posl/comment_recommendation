def main():
    n, m, t = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(m)]
    battery = n
    time = 0
    for i in range(m):
        battery -= ab[i][0] - time
        if battery <= 0:
            print('No')
            return
        battery += ab[i][1] - ab[i][0]
        if battery > n:
            battery = n
        time = ab[i][1]
    battery -= t - time
    if battery <= 0:
        print('No')
    else:
        print('Yes')
