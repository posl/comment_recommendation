def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 1
    for s in S:
        if s == 'OR':
            ans += 2 ** N
        N -= 1
    print(ans)

if __name__ == '__main__':
    main()