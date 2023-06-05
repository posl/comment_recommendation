def main():
    N = 2 ** 20
    A = [0] * N
    Q = int(input())
    for i in range(Q):
        line = input().split()
        t = int(line[0])
        x = int(line[1])
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])
