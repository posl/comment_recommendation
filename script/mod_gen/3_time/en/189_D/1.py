def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 1
    for s in S:
        if s == "AND":
            ans *= 2
        else:
            ans *= 2
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()