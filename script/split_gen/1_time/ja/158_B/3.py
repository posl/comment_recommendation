def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    elif b == 0:
        print(n)
        return
    q, r = divmod(n, a + b)
    ans = a * q + min(a, r)
    print(ans)
