def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == "R":
            ans[i + 1] += 1
        else:
            ans[i] += 1
    ans = list(map(str, ans))
    print(" ".join(ans))

if __name__ == '__main__':
    main()