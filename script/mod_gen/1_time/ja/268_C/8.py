def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    #print(N)
    #print(P)
    P2 = [0] * N
    for i in range(N):
        P2[P[i]] = i
    #print(P2)
    ans = 1
    cnt = 1
    for i in range(1, N):
        if P2[i] < P2[i-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
    ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()