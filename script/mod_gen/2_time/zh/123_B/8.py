def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    a = A
    b = B
    c = C
    d = D
    e = E
    if a % 10 != 0:
        a = a + 10 - a % 10
    if b % 10 != 0:
        b = b + 10 - b % 10
    if c % 10 != 0:
        c = c + 10 - c % 10
    if d % 10 != 0:
        d = d + 10 - d % 10
    if e % 10 != 0:
        e = e + 10 - e % 10
    print(a + b + c + d + e)
main()
