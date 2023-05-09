def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == '.':
            break
        ans += 1
    for i in range(N-1, -1, -1):
        if S[i] == '.':
            break
        ans += 1
    if ans >= N:
        print(N)
        return
    for i in range(N):
        if S[i] == '.':
            break
    for j in range(N-1, -1, -1):
        if S[j] == '.':
            break
    if S[i] == S[j]:
        ans += 1
    ans += 2 * K
    print(min(ans, N))
