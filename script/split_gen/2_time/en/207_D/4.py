def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    if n == 1:
        print("Yes")
        return
    if n == 2:
        if s[0][0] == s[1][0] and s[0][1] == s[1][1]:
            print("Yes")
            return
        if s[0][0] == s[1][1] and s[0][1] == -s[1][0]:
            print("Yes")
            return
        if s[0][0] == -s[1][0] and s[0][1] == -s[1][1]:
            print("Yes")
            return
        if s[0][0] == -s[1][1] and s[0][1] == s[1][0]:
            print("Yes")
            return
        print("No")
        return
    for i in range(n):
        for j in range(n):
            dx = t[i][0] - s[j][0]
            dy = t[i][1] - s[j][1]
            ok = True
            for k in range(n):
                if [s[k][0] + dx, s[k][1] + dy] not in t:
                    ok = False
            if ok:
                print("Yes")
                return
    print("No")
    return
