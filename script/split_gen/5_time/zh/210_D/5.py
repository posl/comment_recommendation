def main():
    h,w,c = map(int,input().split())
    a = [[int(i) for i in input().split()] for _ in range(h)]
    min_cost = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(i,h):
                for l in range(j,w):
                    cost = a[i][j] + a[k][l] + c * (abs(i-k) + abs(j-l))
                    if i == k and j == l:
                        continue
                    min_cost = min(min_cost,cost)
    print(min_cost)
