def main():
    Q = int(input())
    A = [-1 for _ in range(2**20)]
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 2**20] != -1:
                h += 1
            A[h % 2**20] = x
        else:
            print(A[x % 2**20])
