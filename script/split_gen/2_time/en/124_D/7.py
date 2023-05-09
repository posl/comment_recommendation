def main():
    N, K = map(int, input().split())
    S = input()
    L = []
    l = 0
    for i in range(N):
        if i == N-1:
            L.append(i-l+1)
        elif S[i] != S[i+1]:
            L.append(i-l+1)
            l = i+1
    if len(L) == 1:
        print(N)
        return
    if S[0] == "1":
        L = [0] + L
    if S[-1] == "1":
        L = L + [0]
    if len(L) <= 2*K + 1:
        print(N)
        return
    ans = 0
    for i in range(0, len(L)-2*K, 2):
        ans = max(ans, sum(L[i:i+2*K+1]))
    print(ans)
