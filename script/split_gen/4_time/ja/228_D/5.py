def main():
    Q = int(input())
    A = [-1] * 2**20
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            while A[x % 2**20] != -1:
                x += 1
            A[x % 2**20] = x
        elif t == 2:
            print(A[x % 2**20])
