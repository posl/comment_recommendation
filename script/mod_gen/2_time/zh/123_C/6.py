def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    n1 = n // a
    if n % a != 0:
        n1 += 1
    n2 = n1 // b
    if n1 % b != 0:
        n2 += 1
    n3 = n2 // c
    if n2 % c != 0:
        n3 += 1
    n4 = n3 // d
    if n3 % d != 0:
        n4 += 1
    n5 = n4 // e
    if n4 % e != 0:
        n5 += 1
    print(n5 + 4)

if __name__ == '__main__':
    main()