def solve():
    N, A, B = map(int, input().split())
    if N % (A + B) <= A and N % (A + B) != 0:
        print(N // (A + B) * A + N % (A + B))
    else:
        print(N // (A + B) * A + A)

if __name__ == '__main__':
    solve()