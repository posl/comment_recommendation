def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    print(sum(b) - sum(a) + n)

if __name__ == '__main__':
    main()