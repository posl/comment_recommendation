def main():
    n, x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, x + 1):
        if x % i == 0:
            for j in range(n):
                for k in range(l[j][0]):
                    if l[j][k + 1] == i:
                        ans += 1
                        break
    print(ans)

if __name__ == '__main__':
    main()