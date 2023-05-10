def check(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                return True
    return False
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    for j in range(i + 1, m):
        if check(a[i], a[j]):
            print("Yes")
            exit()
print("No")
