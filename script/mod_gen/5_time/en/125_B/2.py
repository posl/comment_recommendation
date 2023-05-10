def main():
    n = int(input())
    v = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    x = 0
    for i in range(n):
        if v[i] > c[i]:
            x += v[i] - c[i]
    print(x)

if __name__ == '__main__':
    main()