def main():
    N = input()
    k = len(N)
    N = int(N)
    if N % 3 == 0:
        print(0)
        return
    for i in range(k-1):
        for j in range(i+1,k):
            if (N - int(N / 10 ** (i+1)) * 10 ** (i+1) - int(N / 10 ** j) * 10 ** j) % 3 == 0:
                print(1)
                return
    for i in range(k-2):
        for j in range(i+1,k-1):
            for l in range(j+1,k):
                if (N - int(N / 10 ** (i+1)) * 10 ** (i+1) - int(N / 10 ** j) * 10 ** j - int(N / 10 ** l) * 10 ** l) % 3 == 0:
                    print(2)
                    return
    print(-1)
    return

if __name__ == '__main__':
    main()