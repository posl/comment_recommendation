def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[-1] = 1
    for i in range(1, N-1):
        if S[i] == "L":
            ans[i-1] += 1
        else:
            ans[i+1] += 1
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()