def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    s = sum(a)
    for i in range(q):
        print(s + x[i] * n)

if __name__ == '__main__':
    main()