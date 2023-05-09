def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] == l[j] or l[j] == l[k] or l[k] == l[i]:
                    continue
                if l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()