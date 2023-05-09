def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    if N == 2:
        print(A[0] ^ A[1])
        return
    if N == 3:
        print(min(A[0] ^ A[1] ^ A[2], A[0] ^ A[1] | A[2], A[0] ^ A[2] | A[1], A[1] ^ A[2] | A[0]))
        return
    if N == 4:
        print(min(A[0] ^ A[1] ^ A[2] ^ A[3], A[0] ^ A[1] ^ A[2] | A[3], A[0] ^ A[1] ^ A[3] | A[2], A[0] ^ A[2] ^ A[3] | A[1], A[1] ^ A[2] ^ A[3] | A[0], A[0] ^ A[1] | A[2] | A[3], A[0] ^ A[2] | A[1] | A[3], A[0] ^ A[3] | A[1] | A[2], A[1] ^ A[2] | A[0] | A[3], A[1] ^ A[3] | A[0] | A[2], A[2] ^ A[3] | A[0] | A[1]))
        return
    if N == 5:
        print(min(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4], A[0] ^ A[1] ^ A[2] ^ A[3] | A[4], A[0] ^ A[1] ^ A[2] ^ A[4] | A[3], A[0] ^ A[1] ^ A[2] | A[3] | A[4], A[0] ^ A[1] ^ A[3] ^ A[4] | A[2], A[0] ^ A[1] ^ A[3] | A[2] | A[4],

if __name__ == '__main__':
    solve()