def main():
    N, T = map(int, input().split())
    lst = []
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            lst.append(c)
    if len(lst) == 0:
        print('TLE')
    else:
        print(min(lst))

if __name__ == '__main__':
    main()