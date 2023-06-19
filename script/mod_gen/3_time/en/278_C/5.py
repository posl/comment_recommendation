def main():
    n, q = map(int, input().split())
    t = []
    a = []
    b = []
    for i in range(q):
        t_i, a_i, b_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
        b.append(b_i)
    follow = []
    for i in range(n):
        follow.append([])
    for i in range(q):
        if t[i] == 1:
            follow[a[i] - 1].append(b[i])
        elif t[i] == 2:
            if b[i] in follow[a[i] - 1]:
                follow[a[i] - 1].remove(b[i])
        elif t[i] == 3:
            if a[i] in follow[b[i] - 1] and b[i] in follow[a[i] - 1]:
                print("Yes")
            else:
                print("No")
main()
