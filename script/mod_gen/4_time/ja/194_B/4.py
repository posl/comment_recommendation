def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                ans = max(ans, a[i]+b[j])
            else:
                ans = max(ans, a[i], b[j])
    print(ans)

if __name__ == '__main__':
    main()