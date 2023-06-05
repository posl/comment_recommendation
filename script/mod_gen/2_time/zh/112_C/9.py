def main():
    N,T = map(int,input().split())
    c = []
    t = []
    for i in range(N):
        a,b = map(int,input().split())
        c.append(a)
        t.append(b)
    if max(t) > T:
        print('TLE')
    else:
        print(min(c))

if __name__ == '__main__':
    main()