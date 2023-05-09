def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        ok = True
        for i in range(n):
            if x < a[i] or x > b[i]:
                ok = False
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()