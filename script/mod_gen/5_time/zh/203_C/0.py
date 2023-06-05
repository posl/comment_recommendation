def main():
    n, k = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a, b = zip(*sorted(zip(a, b), key=lambda x:x[0]))
    # print(a, b)
    ans = k
    for i in range(n):
        if a[i] > ans:
            break
        ans += b[i]
    print(ans)

if __name__ == '__main__':
    main()