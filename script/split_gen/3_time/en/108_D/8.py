def main():
    #print('Hello World')
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, L-1)
    for i in range(1, N):
        print(i, i+1, i)
    for i in range(1, N):
        print(i, i+1, L-i)
    for i in range(1, N):
        print(i, i+1, L-i-1)
