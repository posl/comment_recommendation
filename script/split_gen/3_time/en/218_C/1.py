def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                sx = i
                sy = j
                break
    for i in range(n):
        for j in range(n):
            if t[i][j] == "#":
                tx = i
                ty = j
                break
    dx = tx - sx
    dy = ty - sy
    for i in range(n):
        for j in range(n):
            if 0 <= i + dx < n and 0 <= j + dy < n:
                if s[i][j] != t[i + dx][j + dy]:
                    print("No")
                    return
            else:
                if s[i][j] == "#":
                    print("No")
                    return
    print("Yes")
