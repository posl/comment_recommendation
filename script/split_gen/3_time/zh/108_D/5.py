def main():
    L = int(input())
    N = 2
    M = 2*(L-1)
    print(N, M)
    for i in range(1, L):
        print(i, i+1, 0)
    for i in range(1, L-1):
        print(i, i+2, 2*(i-1)+1)
