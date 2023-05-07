def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(10):
            if S[i][j] == '8':
                ans = max(ans, (i+j)%10)
                break
    print(ans+10)
