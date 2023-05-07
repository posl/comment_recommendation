def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x:x[0])
    ans = []
    for i in range(n):
        if len(ans) == 0:
            ans.append(l[i])
        else:
            if ans[-1][1] >= l[i][1]:
                continue
            elif ans[-1][1] >= l[i][0]:
                ans[-1][1] = l[i][1]
            else:
                ans.append(l[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
