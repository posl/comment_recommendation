def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    s = sum(a)
    for i in range(q):
        print(s + x[i])

if __name__ == '__main__':
    main()