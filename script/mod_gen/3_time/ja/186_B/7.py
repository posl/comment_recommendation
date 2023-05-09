def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    minA = min([min(a) for a in A])
    ans = 0
    for a in A:
        for b in a:
            ans += b - minA
    print(ans)

if __name__ == '__main__':
    main()