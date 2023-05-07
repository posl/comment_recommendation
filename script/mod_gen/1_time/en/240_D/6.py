def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[i] = 0
    d[0] = 1
    for i in range(n):
        d[a[i]-1] += 1
    for i in range(n):
        print(d[i])

if __name__ == '__main__':
    main()