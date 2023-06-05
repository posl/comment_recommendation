def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        s = input()
        a.append(int(s.split()[0]))
        b.append(int(s.split()[1]))
    for i in range(n-1):
        if a[i] == 1:
            print(1, end=' ')
            print(b[i], end=' ')
        elif b[i] == 1:
            print(1, end=' ')
            print(a[i], end=' ')
    print(1)
main()
