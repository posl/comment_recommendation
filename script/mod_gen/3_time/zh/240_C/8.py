def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    sum = 0
    for i in range(n):
        sum += a[i]
    if sum > x:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    solve()