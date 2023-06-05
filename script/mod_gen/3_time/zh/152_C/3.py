def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = p[0]
    for i in range(n):
        if p[i] <= min:
            ans += 1
            min = p[i]
    print(ans)

if __name__ == '__main__':
    main()