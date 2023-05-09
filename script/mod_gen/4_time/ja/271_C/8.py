def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    #print(a)
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()