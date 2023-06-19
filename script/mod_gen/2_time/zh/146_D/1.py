def f(x):
    if x == 0:
        return 1
    else:
        return 0
N = int(input())
a = []
b = []
for i in range(N-1):
    a.append(int(input().split()[0]))
    b.append(int(input().split()[1]))
color = [0] * (N + 1)
color[1] = 1
for i in range(N - 1):
    if color[a[i]] == color[b[i]]:
        color[b[i]] = f(color[b[i]])
    color[b[i]] = color[b[i]]
    color[b[i]+1] = color[b[i]] + 1
    #print(color)
print(max(color))
for i in range(N-1):
    print(color[b[i]])

if __name__ == '__main__':
    f()