def solve(n, q, t, a, b):
    follow = [set() for _ in range(n)]
    for i in range(q):
        if t[i] == 1:
            follow[a[i]-1].add(b[i]-1)
        elif t[i] == 2:
            follow[b[i]-1].add(a[i]-1)
        else:
            if a[i]-1 in follow[b[i]-1]:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    solve()