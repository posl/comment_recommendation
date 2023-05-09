def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    if x[i] == x[j] and x[k] == x[l] and y[i] == y[k] and y[j] == y[l]:
                        ans += 1
    print(ans)
