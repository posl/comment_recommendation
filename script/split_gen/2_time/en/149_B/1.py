def main():
    a, b, k = map(int, input().split())
    if a >= k:
        a -= k
    else:
        k -= a
        a = 0
        if b >= k:
            b -= k
    print(a, b)
