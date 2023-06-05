def main():
    N = int(input())
    S = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]
    first = 0
    for i in range(N):
        if T[i] < T[first]:
            first = i
    ans = [0 for i in range(N)]
    ans[first] = T[first]
    for i in range(first+1, N):
        ans[i] = min(ans[i-1] + S[i-1], T[i])
    for i in range(first):
        ans[i] = min(ans[i-1] + S[i-1], T[i])
    for i in range(N):
        print(ans[i])
main()
