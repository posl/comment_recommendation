def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    if N == 1:
        if M == 0:
            print(0)
        else:
            for i in range(10):
                if [1, i] in sc:
                    print(i)
                    exit()
            print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        else:
            for i in range(10):
                for j in range(10):
                    if [1, i] in sc and [2, j] in sc:
                        print(i*10+j)
                        exit()
            print(-1)
    else:
        if M == 0:
            print(100)
        else:
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        if [1, i] in sc and [2, j] in sc and [3, k] in sc:
                            print(i*100+j*10+k)
                            exit()
            print(-1)

if __name__ == '__main__':
    main()