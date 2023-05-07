def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        a = l[i]
        for j in range(i):
            b = l[j]
            for k in range(j):
                c = l[k]
                if a < b + c:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()