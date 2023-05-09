def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    S_len = len(S)
    T_len = len(T)
    ans = 10**9
    for i in range(S_len-T_len+1):
        cnt = 0
        for j in range(T_len):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()