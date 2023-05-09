def main():
    n = int(input())
    x = list(map(int, input().split()))
    a = 0
    b = 0
    c = 0
    for i in range(n):
        a += abs(x[i])
        b += x[i]**2
        c = max(c, abs(x[i]))
    print(a)
    print(b**(1/2))
    print(c)

if __name__ == '__main__':
    main()