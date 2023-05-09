def main():
    n, m = map(int, input().split())
    data = []
    for i in range(m):
        p, y = map(int, input().split())
        data.append([i, p, y])
    data.sort(key=lambda x: x[2])
    cnt = [0]*n
    ans = [0]*m
    for i in range(m):
        cnt[data[i][1]-1] += 1
        ans[data[i][0]] = '{:06}'.format(data[i][1])+'{:06}'.format(cnt[data[i][1]-1])
    for i in range(m):
        print(ans[i])
