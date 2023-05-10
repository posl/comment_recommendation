def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == "R" and S[i + 1] == "L":
            Rpos = i
            Lpos = i + 1
            Rcnt = 0
            Lcnt = 0
            while S[Rpos] == "R":
                Rpos -= 1
                Rcnt += 1
            while S[Lpos] == "L":
                Lpos += 1
                Lcnt += 1
            if (Rcnt + Lcnt) % 2 == 0:
                ans[i] = Rcnt // 2 + Lcnt // 2
                ans[i + 1] = Rcnt // 2 + Lcnt // 2
            else:
                if Rcnt % 2 == 1:
                    ans[i] = Rcnt // 2 + Lcnt // 2 + 1
                    ans[i + 1] = Rcnt // 2 + Lcnt // 2
                else:
                    ans[i] = Rcnt // 2 + Lcnt // 2
                    ans[i + 1] = Rcnt // 2 + Lcnt // 2 + 1
    print(*ans)

if __name__ == '__main__':
    main()