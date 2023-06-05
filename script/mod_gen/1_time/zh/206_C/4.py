def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * (10**9 + 1)
    for i in a:
        count[i] += 1
    ans = 0
    for i in range(10**9 + 1):
        ans += count[i] * (count[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()