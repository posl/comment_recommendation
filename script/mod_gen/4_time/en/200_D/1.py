def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    for i in range(n):
        b[i] = a[i] % 200
    for i in range(n):
        c[i] = b[i] % 200
    b.sort()
    c.sort()
    if b[0] != b[1]:
        print("Yes")
        print("2")
        print("1", "2")
        print("1", "1")
    else:
        print("Yes")
        print("1")
        print("1")
        print("2")

if __name__ == '__main__':
    main()