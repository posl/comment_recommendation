def main():
    L = int(input())
    N = 0
    M = 0
    for i in range(1,L+1):
        N += i
        M += i-1
    print(N,M)
    for i in range(1,L):
        print(i,i+1,0)
    for i in range(1,L):
        for j in range(i+2,L+1):
            print(i,j,i-1)
