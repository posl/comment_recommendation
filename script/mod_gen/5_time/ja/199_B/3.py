def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        flag = True
        for i in range(n):
            if not a[i] <= x <= b[i]:
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()