def main():
    N = int(input())
    P = list(map(int, input().split()))
    for i in range(N):
        P[i] = (P[i] - i) % N
    #print(P)
    cnt = [0] * N
    for p in P:
        cnt[p] += 1
    #print(cnt)
    print(max(cnt))

if __name__ == '__main__':
    main()