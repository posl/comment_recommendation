def main():
    N = int(input())
    A = [0 for i in range(N)]
    B = [0 for i in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        A[i] = a
        B[i] = b
    #prin
