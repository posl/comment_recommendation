def main():
    N = int(input())
    li = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            li.append([l, r])
        elif t == 2:
            li.append([l, r - 1])
        elif t == 3:
            li.append([l + 1, r])
        else:
            li.append([l + 1, r - 1])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if li[i][0] <= li[j][1] and li[j][0] <= li[i][1]:
                ans += 1
    print(ans)
