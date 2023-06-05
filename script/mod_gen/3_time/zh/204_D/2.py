def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    ans = 0
    for i in range(n):
        ans = max(ans, sum(t[:i+1]) + t[i]//2)
    print(ans)

if __name__ == '__main__':
    main()