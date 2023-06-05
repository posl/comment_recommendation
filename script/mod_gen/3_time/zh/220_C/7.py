def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    S = sum(A)
    if S >= X:
        print(N)
        return
    k = (X - S) // min(A)
    print(N + k)

if __name__ == '__main__':
    solve()