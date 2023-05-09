def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    ans = []
    for i in range(H):
        if a[i].count("#") > 0:
            ans.append(a[i])
    ans2 = []
    for i in range(len(ans[0])):
        cnt = 0
        for j in range(len(ans)):
            if ans[j][i] == "#":
                cnt += 1
        if cnt > 0:
            ans2.append(i)
    for i in range(len(ans)):
        for j in range(len(ans2)):
            print(ans[i][ans2[j]], end="")
        print()
