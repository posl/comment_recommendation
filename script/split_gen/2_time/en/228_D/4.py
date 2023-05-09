def main():
    N = 2**20
    A = [-1]*N
    Q = int(input())
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
        elif t == 2:
            print(A[x%N])
