def main():
    x, y, r = map(float, input().split())
    ans = 0
    for i in range(int(x - r), int(x + r) + 1):
        for j in range(int(y - r), int(y + r) + 1):
            if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()