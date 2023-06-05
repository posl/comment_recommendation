def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    ans = 0
    for i in range(n//2):
        if d[i] != d[i+n//2]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()