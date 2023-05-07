def main():
    A, B, C, X = map(int, input().split())
    ans = 0
    ans += (X >= A) * (1 - (B - X) / (B - A))
    ans += (X >= A + 1) * (C / (B - A))
    print(ans)

if __name__ == '__main__':
    main()