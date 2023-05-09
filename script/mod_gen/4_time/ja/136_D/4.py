def main():
    # input
    S = input()
    N = len(S)
    # compute
    ans = [0] * N
    for i in range(N):
        if S[i] == "R":
            if i % 2 == 0:
                ans[i+1] += 1
            else:
                ans[i-1] += 1
        else:
            if i % 2 == 0:
                ans[i-1] += 1
            else:
                ans[i+1] += 1
    # output
    print(*ans)

if __name__ == '__main__':
    main()