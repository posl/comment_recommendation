def solve(a, b, k):
    #print(a, b, k)
    #print("a", a, "b", b, "k", k)
    if a == 0:
        return "b" * b
    if b == 0:
        return "a" * a
    #print("a", a, "b", b, "k", k)
    c = comb(a - 1 + b, a - 1)
    #print("c", c)
    if k <= c:
        return "a" + solve(a - 1, b, k)
    else:
        return "b" + solve(a, b - 1, k - c)

if __name__ == '__main__':
    solve()