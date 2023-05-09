def main():
    L = int(input())
    N = 2
    while 2**N <= L:
        N += 1
    M = N + L - 1
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(N-1):
        if L & 1:
            print(i+1, i+2, 2**(N-1-i))
        L >>= 1
