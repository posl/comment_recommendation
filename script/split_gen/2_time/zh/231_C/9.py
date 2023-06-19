def solve(n, q, a, x):
    a.sort()
    for i in range(q):
        print(binary_search(a, x[i]))
