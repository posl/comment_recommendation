def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    a.sort()
    ans = "No"
    for i in range(m-1):
        for j in range(i+1,m):
            if a[i][0] == a[j][0]:
                continue
            if a[i][1] == a[j][1]:
                ans = "Yes"
                break
    print(ans)
