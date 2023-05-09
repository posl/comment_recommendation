def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    if sum(a) <= X and X <= sum(b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()