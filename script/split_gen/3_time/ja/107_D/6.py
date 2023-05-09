def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        for j in range(i,N):
            b.append(a[i:j+1])
    b.sort()
    print(b[int((N*(N+1))/2)])
