def main():
    n,m,t = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    battery = n
    for i in range(m):
        if i == 0:
            battery -= ab[i][0]
        else:
            battery -= ab[i][0] - ab[i-1][1]
        if battery <= 0:
            print('No')
            exit()
        battery += ab[i][1] - ab[i][0]
        if battery > n:
            battery = n
    if battery - (t - ab[m-1][1]) <= 0:
        print('No')
    else:
        print('Yes')
main()
