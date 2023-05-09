def main():
    a, b = map(int, input().split())
    if a < b:
        print(a)
        return
    x = int(a ** 0.5)
    if x * (x + 1) < a:
        x += 1
    ans = 10 ** 18
    for i in range(x):
        ans = min(ans, (a + i) / (x + i))
    print(ans)

if __name__ == '__main__':
    main()