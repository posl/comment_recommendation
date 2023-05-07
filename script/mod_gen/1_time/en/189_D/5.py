def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 2**N
    for i in range(N):
        if S[i] == "AND":
            ans -= 2**(N-i-1)
    print(ans)

if __name__ == '__main__':
    main()