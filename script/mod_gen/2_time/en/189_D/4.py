def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**N):
        y = (i >> N-1) & 1
        for j in range(N):
            x = (i >> N-j-1) & 1
            if S[j] == "AND":
                y = y & x
            else:
                y = y | x
        if y == 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()