def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    T = [0 for i in range(N)]
    T[X-1] = 1
    for i in range(N):
        if T[A[i]-1] == 1:
            T[i] = 1
    print(sum(T))
