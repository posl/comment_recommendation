def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # 逆向思维，从后往前找，即从N开始
    ans = [i for i in range(1,n+1)]
    for i in range(m):
        if ans.index(a[m-1-i]) < ans.index(b[m-1-i]):
            continue
        else:
            ans.remove(a[m-1-i])
            ans.insert(ans.index(b[m-1-i]), a[m-1-i])
    print(*ans)

if __name__ == '__main__':
    main()