def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    n = len(S)
    m = len(T)
    ans = 1000
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()