def main():
    N = int(input())
    x = [0]*N
    y = [0]*N
    for i in range(N):
        x[i],y[i] = map(int,input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (x[j]-x[i])*(y[k]-y[i]) == (y[j]-y[i])*(x[k]-x[i]):
                    continue
                for l in range(k+1,N):
                    if (x[k]-x[j])*(y[l]-y[j]) == (y[k]-y[j])*(x[l]-x[j]):
                        continue
                    if (x[l]-x[k])*(y[i]-y[k]) == (y[l]-y[k])*(x[i]-x[k]):
                        continue
                    if (x[i]-x[l])*(y[j]-y[l]) == (y[i]-y[l])*(x[j]-x[l]):
                        continue
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()