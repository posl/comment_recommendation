def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_a = min([min(a) for a in A])
    ans = 0
    for a in A:
        for aa in a:
            ans += aa - min_a
    print(ans)

if __name__ == '__main__':
    main()