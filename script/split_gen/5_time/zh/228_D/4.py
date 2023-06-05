def main():
    n = 2**20
    A = [-1] * n
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % n] != -1:
                h += 1
            A[h % n] = x
        else:
            print(A[x % n])
