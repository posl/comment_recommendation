def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(10):
        cnt = [0]*10
        for j in range(N):
            cnt[(int(S[j][i])+i)%10] += 1
        ans += N - max(cnt)
    print(ans)

if __name__ == '__main__':
    main()