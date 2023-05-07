def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "L":
            r = i
            for j in range(i-1, -1, -1):
                if S[j] == "R":
                    l = j
                    break
            else:
                l = -1
        else:
            l = i
            for j in range(i+1, N):
                if S[j] == "L":
                    r = j
                    break
            else:
                r = N
        ans = max(ans, r - l - 1)
    print(min(ans + 2*K, N))

if __name__ == '__main__':
    main()