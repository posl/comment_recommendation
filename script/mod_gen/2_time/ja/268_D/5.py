def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = ""
    for i in range(3, 17):
        for j in range(2 ** (i - 1)):
            tmp = ""
            for k in range(i - 1):
                if j >> k & 1:
                    tmp += "_"
                tmp += S[k]
            tmp += S[i - 1]
            if tmp not in T:
                ans = tmp
                break
        if ans:
            break
    print(ans if ans else -1)

if __name__ == '__main__':
    main()