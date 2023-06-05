def main():
    n = int(input())
    l = []
    for i in range(n):
        t, l1, l2 = map(int, input().split())
        if t == 1:
            l.append([l1, l2])
        elif t == 2:
            l.append([l1, l2-1])
        elif t == 3:
            l.append([l1+1, l2])
        elif t == 4:
            l.append([l1+1, l2-1])
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[i][0] <= l[j][1] and l[j][0] <= l[i][1]:
                ans += 1
    print(ans)
