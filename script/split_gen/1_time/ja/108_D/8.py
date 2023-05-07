def main():
    L = int(input())
    N = 2*L
    M = 2*L-1
    print(N,M)
    for i in range(1,N):
        print(i,i+1,0)
    for i in range(1,L+1):
        print(i,N-i+1,i)
