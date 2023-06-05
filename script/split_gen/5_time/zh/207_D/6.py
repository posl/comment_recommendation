def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = map(int, input().split())
        s.append([a, b])
    for i in range(n):
        c, d = map(int, input().split())
        t.append([c, d])
    s.sort()
    t.sort()
    for i in range(n):
        s[i][0] -= t[0][0]
        s[i][1] -= t[0][1]
    for i in range(n):
        for j in range(n):
            if s[i][0] == t[j][0] and s[i][1] == t[j][1]:
                flag = 1
                for k in range(n):
                    if s[(i+k)%n][0] != t[(j+k)%n][0] or s[(i+k)%n][1] != t[(j+k)%n][1]:
                        flag = 0
                        break
                if flag == 1:
                    print('Yes')
                    return
    print('No')
