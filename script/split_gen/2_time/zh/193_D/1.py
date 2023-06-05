def main():
    n = int(input())
    a = 2
    b = 2
    s = set()
    while a**b <= n:
        while a**b <= n:
            s.add(a**b)
            b += 1
        a += 1
        b = 2
    print(n-len(s))
