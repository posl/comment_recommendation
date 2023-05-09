def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                continue
            for k in range(j + 1, n):
                if s[i][k] == "#":
                    continue
                for l in range(i + 1, n):
                    if s[l][j] == "#":
                        continue
                    if s[l][k] == "#":
                        continue
                    print("Yes")
                    return
    print("No")
