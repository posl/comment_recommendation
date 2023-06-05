def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for x in range(0, 200):
        #print(x)
        cnt = 0
        for i in range(N):
            if S[i] == '0' and W[i] <= x:
                cnt += 1
            if S[i] == '1' and W[i] > x:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
