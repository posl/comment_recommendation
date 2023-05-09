def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, A, B)
    AB = [(a+b, a, b) for a, b in zip(A, B)]
    AB.sort(reverse=True)
    #print(AB)
    takahashi = 0
    aoki = 0
    for ab in AB:
        takahashi += ab[1]
        aoki += ab[2]
        if takahashi > aoki:
            print(AB.index(ab)+1)
            return
    print(N)

if __name__ == '__main__':
    main()