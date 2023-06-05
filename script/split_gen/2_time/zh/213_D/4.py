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
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i + 1
    for i in range(len(b)):
        b_dict[b[i]] = i + 1
    for i in range(n):
        print(a_dict[a[i]], b_dict[b[i]])
