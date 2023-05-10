def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    if len(a_set) == 1:
        print(0)
        exit()
    
    a.sort()
    ans = 0
    for i in range(n//2):
        if a[i] != a[n-1-i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()