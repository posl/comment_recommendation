def jump(i, x):
    if i >= N:
        return False
    if x == X:
        return True
    return jump(i + 1, x + a[i]) or jump(i + 1, x + b[i])
N, X = map(int, input().split())
a = []
b = []
for i in range(N):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)
print("Yes" if jump(0, 0) else "No")
