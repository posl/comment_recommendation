def find_root(f, x0):
    x = x0
    for i in range(100):
        x = f(x)
    return x
N = int(input())
x = []
y = []
p = []
for i in range(N):
    tmp = input().split()
    x.append(int(tmp[0]))
    y.append(int(tmp[1]))
    p.append(int(tmp[2]))
