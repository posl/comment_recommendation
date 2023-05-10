def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = list(set(a))
    a.sort()
    a = a[::-1]
    a2 = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 4 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 8 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 16 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 32 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 64 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 128 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 256 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 512 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 1024 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] == 2:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] == 4:
            a2.append(a[i])
    a = a2
    a

if __name__ == '__main__':
    main()