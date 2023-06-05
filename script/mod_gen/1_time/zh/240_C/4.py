def solve():
    # N X
    N, X = map(int, input().split())
    # a_1 b_1
    # .
    # .
    # .
    # a_N b_N
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(N, X)
    # print(a)
    # print(b)
    # 求和
    sum = 0
    for i in range(N):
        sum += a[i]
        sum += b[i]
    # print(sum)
    # 判断
    if sum >= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()