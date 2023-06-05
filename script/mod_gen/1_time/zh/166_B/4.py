def main():
    n, k = map(int, input().split())
    l = [0] * n
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for j in range(d):
            l[a[j] - 1] += 1
    print(l.count(0))

if __name__ == '__main__':
    main()