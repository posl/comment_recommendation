def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    a = int(pow(n, 1/3))
    for b in range(a+1):
        if a**3+a**2*b+a*b**2+b**3 == n:
            print(a**3+a**2*b+a*b**2+b**3)
            return
        if a**3+a**2*b+a*b**2+b**3 > n:
            print(a**3+a**2*b+a*b**2+b**3)
            return
        if a**3+a**2*b+a*b**2+b**3 < n:
            continue
    print(a**3+a**2*b+a*b**2+b**3)
    return
main()
