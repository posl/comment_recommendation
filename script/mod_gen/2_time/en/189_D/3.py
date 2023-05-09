def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2 ** (N + 1)):
        s = bin(i)[2:].zfill(N + 1)
        flag = True
        for j in range(N):
            if S[j] == "AND":
                if s[j] == "1" and s[j + 1] == "1":
                    pass
                else:
                    flag = False
                    break
            else:
                if s[j] == "0" and s[j + 1] == "0":
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()