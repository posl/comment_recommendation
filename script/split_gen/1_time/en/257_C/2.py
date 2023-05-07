def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, 10**9):
        cnt = 0
        for j in range(N):
            if S[j] == '0' and W[j] < i:
                cnt += 1
            elif S[j] == '1' and W[j] >= i:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
