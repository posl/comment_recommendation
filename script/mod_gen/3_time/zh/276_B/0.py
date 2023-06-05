def solve():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort(key=lambda x:x[1])
    roads.sort(key=lambda x:x[0])
    ans = [[] for i in range(n)]
    for i in range(m):
        ans[roads[i][0]-1].append(roads[i][1])
        ans[roads[i][1]-1].append(roads[i][0])
    for i in range(n):
        ans[i].insert(0, len(ans[i]))
        print(" ".join(map(str, ans[i])))

if __name__ == '__main__':
    solve()