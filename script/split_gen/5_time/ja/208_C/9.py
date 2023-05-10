def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0 for i in range(N)]
    for i in range(N):
        b[a[i]-1] = i
    c = [0 for i in range(N)]
    for i in range(N):
        c[i] = K//N
    for i in range(K%N):
        c[b[i]] += 1
    for i in range(N):
        print(c[i])
