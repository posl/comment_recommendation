def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    count = 0
    for i in range(N):
        if X >= a[i] and X <= b[i]:
            count += 1
    if count > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()