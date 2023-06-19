def main():
    h1, w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int, input().split())))
    for i in range(h1):
        for j in range(w1):
            if a[i][j] in b:
                b.remove(a[i][j])
    if len(b) == 0:
        print('Yes')
    else:
        print('No')
