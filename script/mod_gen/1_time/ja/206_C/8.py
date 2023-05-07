def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    ans = 0
    for i in range(n):
        if i == n-1:
            break
        if a[i] == a[i+1]:
            continue
        ans += n-i-1
    print(ans)

if __name__ == '__main__':
    main()