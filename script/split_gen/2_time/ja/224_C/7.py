def main():
    N = int(input())
    x = [0]*N
    y = [0]*N
    for i in range(N):
        x[i],y[i] = map(int, input().split())
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if (y[k]-y[i])*(x[j]-x[i]) != (y[j]-y[i])*(x[k]-x[i]):
                    ans += 1
    print(ans)
