def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 'No'
    for i in range(n):
        if x == a[i] * b[i]:
            ans = 'Yes'
            break
        for j in range(n):
            if x == a[i] * b[i] + a[j] * b[j]:
                ans = 'Yes'
                break
    print(ans)

if __name__ == '__main__':
    main()