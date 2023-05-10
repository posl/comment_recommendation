def main():
    Q = int(input())
    A = [-1]*(2**20)
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h%len(A)] != -1:
                h += 1
            A[h%len(A)] = x
        else:
            print(A[x%len(A)])
