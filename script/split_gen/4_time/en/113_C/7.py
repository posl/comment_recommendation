def main():
    # Get input here
    N, M = map(int, input().split())
    py = []
    for i in range(M):
        p, y = map(int, input().split())
        py.append((p, y, i))
    # Calculate desired output below
    py.sort(key=lambda x:(x[0], x[1]))
    p = 0
    x = 1
    ans = []
    for i in range(M):
        if p == py[i][0]:
            x += 1
        else:
            x = 1
        p = py[i][0]
        ans.append((py[i][2], p, x))
    ans.sort(key=lambda x:x[0])
    for i in range(M):
        print('{0:06}{1:06}'.format(ans[i][1], ans[i][2]))
    # Print output here
