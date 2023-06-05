def main():
    n, m = map(int, input().split())
    k = [0] * m
    a = [[] for _ in range(m)]
    for i in range(m):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    print(k, a)

if __name__ == '__main__':
    main()