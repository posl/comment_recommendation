def main():
    h,w,c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_cost = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(i+1, h):
                for l in range(j+1, w):
                    min_cost = min(min_cost, a[i][j]+a[k][l]+c*(abs(i-k)+abs(j-l)))
    print(min_cost)
