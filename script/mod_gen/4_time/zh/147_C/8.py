def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        for j in range(a[i]):
            x, y = map(int, input().split())
    ans = 0
    for i in range(2 ** n):
        flag = True
        for j in range(n):
            if i >> j & 1:
                for k in range(a[j]):
                    if (i >> (x - 1)) & 1 ^ y:
                        flag = False
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()