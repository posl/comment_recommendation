def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i, a in enumerate(A):
        B[a-1] = str(i+1)
    print(" ".join(B))

if __name__ == '__main__':
    solve()