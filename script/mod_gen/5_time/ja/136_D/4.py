def main():
    S = input()
    N = len(S)
    ans = [0] * N
    cnt = 1
    for i in range(N-1):
        if S[i] == "R" and S[i+1] == "L":
            ans[i] += cnt//2
            ans[i+1] += cnt//2
            cnt = 1
        elif S[i] == "R" and S[i+1] == "R":
            cnt += 1
        elif S[i] == "L" and S[i+1] == "L":
            cnt += 1
        else:
            ans[i] += cnt//2
            ans[i+1] += cnt//2
            cnt = 1
    print(*ans)

if __name__ == '__main__':
    main()