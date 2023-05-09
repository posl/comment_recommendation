def main():
    A, B, C = map(int, input().split())
    ans = 0
    ans += A * (A + B + C - 1) / (A + B + C) / (A + B + C - 1)
    ans += B * (A + B + C - 1) / (A + B + C) / (A + B + C - 1)
    ans += C * (A + B + C - 1) / (A + B + C) / (A + B + C - 1)
    ans += 1
    print(ans)

if __name__ == '__main__':
    main()