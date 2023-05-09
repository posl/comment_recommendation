def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(2 ** n):
        cnt = 0
        for j in range(n):
            if i & (1 << j):
                cnt += a[j][0] * a[j][1]
        if cnt == x:
            print("Yes")
            break
    else:
        print("No")
