def main():
    N, T = map(int, input().split())
    C = []
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            C.append(c)
    if C:
        print(min(C))
    else:
        print('TLE')

if __name__ == '__main__':
    main()