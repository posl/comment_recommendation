def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    ans = t[0]
    for i in range(n-1):
        ans += t[i+1]
    print(ans)

if __name__ == '__main__':
    main()