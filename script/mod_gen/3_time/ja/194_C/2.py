def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        for j in range(i):
            s += (a[i] - a[j]) ** 2
    print(s)

if __name__ == '__main__':
    main()