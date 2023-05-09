def main():
    N = 2**20
    A = [-1] * N
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        x %= N
        if t == 1:
            while A[x] != -1:
                x += 1
                x %= N
            A[x] = x
        else:
            print(A[x])
    return
