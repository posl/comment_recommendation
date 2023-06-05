def main():
    N,M = map(int,input().split())
    s = [0 for i in range(M)]
    c = [0 for i in range(M)]
    for i in range(M):
        s[i],c[i] = map(int,input().split())
    if N == 1:
        for i in range(10):
            if i == c[0]:
                print(i)
                exit()
        print(-1)
        exit()
    if N == 2:
        for i in range(10):
            for j in range(10):
                if i == c[0] and j == c[1]:
                    print(i*10+j)
                    exit()
        print(-1)
        exit()
    if N == 3:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == c[0] and j == c[1] and k == c[2]:
                        print(i*100+j*10+k)
                        exit()
        print(-1)
        exit()

if __name__ == '__main__':
    main()