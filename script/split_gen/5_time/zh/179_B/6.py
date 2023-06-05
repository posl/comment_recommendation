def check(n, d):
    for i in range(n-2):
        if d[i][0]==d[i][1] and d[i+1][0]==d[i+1][1] and d[i+2][0]==d[i+2][1]:
            return True
    return False
n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
print("Yes" if check(n, d) else "No")
