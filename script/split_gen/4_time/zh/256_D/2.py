def main():
    n = int(input())
    lrs = []
    for i in range(n):
        lrs.append(list(map(int, input().split())))
    lrs.sort(key=lambda x: x[0])
    ans = []
    ans.append(lrs[0])
    for i in range(1, n):
        if lrs[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], lrs[i][1])
        else:
            ans.append(lrs[i])
    for i in ans:
        print(i[0], i[1])
