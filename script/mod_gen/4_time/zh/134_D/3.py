def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    b = [0]*N
    c = [0]*N
    d = []
    for i in range(N):
        if a[i] == 1:
            d.append(i+1)
    M = len(d)
    if M == 0:
        print(0)
        return
    for i in range(M):
        for j in range(M):
            if d[i] % d[j] == 0:
                b[i] += 1
    for i in range(M):
        if b[i] % 2 == 1:
            print(-1)
            return
    print(M)
    for i in range(M):
        print(d[i])

if __name__ == '__main__':
    main()