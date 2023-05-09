def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
N,K = map(int, input().split())
A = list(map(int, input().split()))
P = [tuple(map(int, input().split())) for _ in range(N)]
L = [dist(P[i-1],P[j-1]) for i in range(1,N+1) for j in A]
print(max(L))

if __name__ == '__main__':
    dist()