def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    l = 0
    for i in range(n):
        if a[i] == a[i+1]:
            l += 1
        else:
            ans += l * (l-1) // 2
            l = 0
    print(ans)

if __name__ == '__main__':
    main()