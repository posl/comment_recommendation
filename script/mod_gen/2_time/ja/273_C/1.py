def solve():
    from collections import defaultdict
    N = int(input())
    A = list(map(int, input().split()))
    B = defaultdict(int)
    for a in A:
        B[a] += 1
    C = [0] * N
    for i in B:
        C[B[i]-1] += 1
    for i in C:
        print(i)

if __name__ == '__main__':
    solve()