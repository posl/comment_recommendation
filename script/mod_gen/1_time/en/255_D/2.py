def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    print(n, q)
    print(a)
    print(x)
    for i in range(q):
        print(x[i])

if __name__ == '__main__':
    main()