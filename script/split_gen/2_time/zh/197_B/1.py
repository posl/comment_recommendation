def check(a, b, c, d, s):
    #print("check", a, b, c, d)
    if a == c:
        #print("same row")
        if b > d:
            #print("reverse")
            b, d = d, b
        for i in range(b, d + 1):
            if s[a][i] == "#":
                return False
        return True
    elif b == d:
        #print("same column")
        if a > c:
            #print("reverse")
            a, c = c, a
        for i in range(a, c + 1):
            if s[i][b] == "#":
                return False
        return True
    else:
        #print("not same")
        return False
H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
ans = 1
for i in range(X - 2, -1, -1):
    if S[i][Y - 1] == "#":
        break
    else:
        ans += 1
for i in range(X, H):
    if S[i][Y - 1] == "#":
        break
    else:
        ans += 1
for i in range(Y - 2, -1, -1):
    if S[X - 1][i] == "#":
        break
    else:
        ans += 1
for i in range(Y, W):
    if S[X - 1][i] == "#":
        break
    else:
        ans += 1
print(ans)
