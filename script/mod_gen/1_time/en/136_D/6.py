def main():
    S = input()
    N = len(S)
    ans = [0] * N
    child = 0
    for i in range(N):
        if S[i] == "R":
            child += 1
        else:
            ans[i] = child // 2
            ans[i - 1] = child - ans[i]
            child = 0
    ans[0] = child
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()