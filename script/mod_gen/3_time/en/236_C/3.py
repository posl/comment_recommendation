def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    ans = []
    for i in range(N):
        if S[i] in T:
            ans.append("Yes")
        else:
            ans.append("No")
    print(*ans, sep = "
")

if __name__ == '__main__':
    main()