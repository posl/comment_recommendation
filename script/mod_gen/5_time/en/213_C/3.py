def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a_sorted = sorted(list(set(a)))
    b_sorted = sorted(list(set(b)))
    a_dict = dict(zip(a_sorted, range(1, len(a_sorted) + 1)))
    b_dict = dict(zip(b_sorted, range(1, len(b_sorted) + 1)))
    for i in range(n):
        print(a_dict[a[i]], b_dict[b[i]])

if __name__ == '__main__':
    main()