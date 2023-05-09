def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i],y[i] = map(int,input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (x[j]-x[i])*(y[k]-y[i]) - (x[k]-x[i])*(y[j]-y[i]) != 0:
                    ans += 1
    print(ans)
