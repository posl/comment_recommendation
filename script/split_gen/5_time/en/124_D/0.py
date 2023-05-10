def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            ans += 1
    ans += min(count, K) * 2
    if K >= count:
        ans += 1
    print(ans)
