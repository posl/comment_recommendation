def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = []
    for i in range(k):
        d[i] = int(input())
        a.append(list(map(int, input().split())))
    a = sum(a, [])
    a = set(a)
    print(n - len(a))

if __name__ == '__main__':
    main()