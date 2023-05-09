def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    ans = []
    left = l[0][0]
    right = l[0][1]
    for i in range(1,n):
        if right < l[i][0]:
            ans.append([left,right])
            left = l[i][0]
            right = l[i][1]
        elif right < l[i][1]:
            right = l[i][1]
    ans.append([left,right])
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])
