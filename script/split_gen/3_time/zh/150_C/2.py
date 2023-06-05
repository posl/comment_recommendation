def permutation(n, start, end):
    if start == end:
        print(n)
    else:
        for i in range(start, end):
            n[start], n[i] = n[i], n[start]
            permutation(n, start + 1, end)
            n[start], n[i] = n[i], n[start]
