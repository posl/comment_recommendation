def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    for i in range(n):
        t.append(list(map(int, input().split())))
    s.sort()
    t.sort()
    sx = s[0][0]
    sy = s[0][1]
    tx = t[0][0]
    ty = t[0][1]
    for i in range(n):
        s[i][0] -= sx
        s[i][1] -= sy
        t[i][0] -= tx
        t[i][1] -= ty
    if s == t:
        print("Yes")
    else:
        print("No")
