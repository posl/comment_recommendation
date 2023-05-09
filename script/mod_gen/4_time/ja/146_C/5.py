def main():
    a, b, x = map(int, input().split())
    ans = 0
    for i in range(1, 10):
        if x < a * 10 ** i + b * i:
            ans = i - 1
            break
    if x >= a * 10 ** 9 + b * 10:
        ans = 10 ** 9
    print(ans)

if __name__ == '__main__':
    main()