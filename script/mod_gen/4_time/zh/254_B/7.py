def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0] + L, L + [0])]
n = int(input())
for i in triangles():
    print(i)
    if len(i) == n:
        break

if __name__ == '__main__':
    triangles()