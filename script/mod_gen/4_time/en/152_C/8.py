def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N, P)
    #print(P.index(1))
    #print(P.index(2))
    #print(P.index(3))
    #print(P.index(4))
    #print(P.index(5))
    #print(P.index(6))
    #print(P.index(7))
    #print(P.index(8))
    cnt = 1
    min = P[0]
    for i in range(1, N):
        if min >= P[i]:
            cnt += 1
            min = P[i]
    print(cnt)

if __name__ == '__main__':
    main()