def main():
    (N,X) = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]*(N+1)
    for i in range(1,N+1):
        D[i] = D[i-1] + L[i-1]
    i = 0
    while D[i] <= X:
        i += 1
    print(i)
