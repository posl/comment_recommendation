def solve(h, w, n, ab):
    a = []
    b = []
    for i in range(n):
        a.append(ab[i][0])
        b.append(ab[i][1])
    a.sort()
    b.sort()
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i+1
    for i in range(len(b)):
        b_dict[b[i]] = i+1
    for i in range(n):
        print(a_dict[ab[i][0]], b_dict[ab[i][1]])
