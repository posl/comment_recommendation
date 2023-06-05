def solve(n, q, a, k):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print("Hello world!")
    if n < q:
        return
    index = 0
    for i in range(q):
        while True:
            index += 1
            if index not in a:
                k[i] -= 1
            if k[i] == 0:
                break
    return index
