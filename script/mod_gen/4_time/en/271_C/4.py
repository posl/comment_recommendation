def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 1
    for i in range(n):
        if a[i] <= ans:
            ans += a[i]
        else:
            break
    print(ans)
    return

if __name__ == '__main__':
    main()