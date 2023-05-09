def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if b[i][j] != (i-1)*7 + j + 1:
                print("No")
                exit()
    print("Yes")
