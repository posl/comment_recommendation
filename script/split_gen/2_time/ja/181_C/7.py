def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 'No'
    for i in range(N):
        for j in range(N):
            if i == j: continue
            for k in range(N):
                if k == j or k == i: continue
                if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                    ans = 'Yes'
    print(ans)
