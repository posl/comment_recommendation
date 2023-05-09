def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    ans = M
    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            if S[i+j] != T[j]:
                tmp += 1
        ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()