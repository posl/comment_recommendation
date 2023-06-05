def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a = {a[i]:i+1 for i in range(len(a))}
    b = {b[i]:i+1 for i in range(len(b))}
    for i in range(n):
        print(a[a[i+1]], b[b[i+1]])
