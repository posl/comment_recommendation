def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    S = [sum(p) for p in P]
    ans = [0]*N
    for i in range(N):
        ans[i] = sum([1 for s in S if S[i] < s])+1
    for a in ans:
        if a <= K:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()