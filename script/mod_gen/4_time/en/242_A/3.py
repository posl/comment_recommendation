def main():
    A, B, C, X = map(int, input().split())
    ans = 0
    if X >= A:
        ans += (B - A + 1)
        if X >= B:
            ans += (B - A + 1) * C
    print(ans / 1000)

if __name__ == '__main__':
    main()