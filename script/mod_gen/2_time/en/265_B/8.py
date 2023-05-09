def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    rooms = [list(map(int, input().split())) for i in range(m)]
    now = 0
    for i in range(n-1):
        t -= a[i] - now
        if t <= 0:
            print('No')
            return
        for room in rooms:
            if room[0] == i + 2:
                t += room[1]
                if t > 10**9:
                    t = 10**9
        now = a[i]
    t -= a[n-1] - now
    if t <= 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()