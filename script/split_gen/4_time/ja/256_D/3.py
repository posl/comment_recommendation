def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    ans = []
    ans.append(l[0])
    for i in range(1, n):
        if ans[-1][1] >= l[i][0]:
            ans[-1][1] = max(ans[-1][1], l[i][1])
        else:
            ans.append(l[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
