def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = 0
    d = 0
    for i in range(n):
        if a[i] == b[i]:
            c += 1
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i] == b[j]:
                    d += 1
    print(c)
    print(d // 2)

if __name__ == '__main__':
    main()