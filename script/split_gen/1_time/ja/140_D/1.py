def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == 'L':
            cnt = 0
            for j in range(i, -1, -1):
                if S[j] == 'L':
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
        else:
            cnt = 0
            for j in range(i, N):
                if S[j] == 'R':
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
    print(min(ans + 2 * K, N))
