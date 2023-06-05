def judge(x, y):
    for i in range(x+1):
        if 2*i + 4*(x-i) == y:
            return True
    return False
x, y = map(int, input().split())
print("Yes" if judge(x, y) else "No")
