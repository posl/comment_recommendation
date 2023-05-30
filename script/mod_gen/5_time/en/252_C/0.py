def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(10):
        cnt = 0
        for j in range(N):
            if S[j][i] == str(i):
                cnt += 1
        if cnt > ans:
            ans = cnt
    print(ans)
main()
