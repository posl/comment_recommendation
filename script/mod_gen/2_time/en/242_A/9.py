def main():
    A, B, C, X = map(int, input().split())
    ans = 0
    ans += max(0, X - A + 1) * max(0, B - X + 1)
    ans += max(0, X - A) * max(0, B - X)
    ans -= max(0, X - A) * max(0, B - X) * (C / (B - A + 1))
    ans /= (B - A + 1) * (B - A + 1)
    print(ans)

if __name__ == '__main__':
    main()