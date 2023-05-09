def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = [0] * 200
    for i in a:
        m[i % 200] += 1
    ans = 0
    for i in m:
        ans += i * (i - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()