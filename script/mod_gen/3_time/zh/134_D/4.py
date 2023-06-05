def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    b = []
    for i in range(n):
        if a[i] == 1:
            s += 1
            b.append(i + 1)
    if s == 0:
        print(0)
    else:
        print(s)
        print(*b)

if __name__ == '__main__':
    main()