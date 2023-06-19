def main():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(n):
        k.append(list(map(int, input().split())))
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(m):
        flag = True
        for j in range(n):
            if i + 1 not in a[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()