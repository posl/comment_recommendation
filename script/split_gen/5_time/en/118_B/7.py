def main():
    N,M = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(N)]
    A = [a[1:] for a in A]
    A = set(A[0]).intersection(*A)
    print(len(A))
