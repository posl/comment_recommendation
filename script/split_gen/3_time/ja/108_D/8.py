def main():
    L = int(input())
    N = 2*L+1
    print(N,N-1)
    for i in range(1,N):
        print(i, i+1, 0)
    for i in range(1,L+1):
        print(i, i+L, 1)
