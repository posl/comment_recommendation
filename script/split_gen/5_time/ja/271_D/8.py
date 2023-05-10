def main():
    n, s = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1 << n):
        t = 0
        for j in range(n):
            if (i >> j) & 1:
                t += a[j][1]
            else:
                t += a[j][0]
        if t == s:
            print("Yes")
            for j in range(n):
                if (i >> j) & 1:
                    print("T", end="")
                else:
                    print("H", end="")
            print()
            exit()
    print("No")
