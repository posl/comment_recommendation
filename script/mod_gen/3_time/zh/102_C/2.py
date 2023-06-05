def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - (i + 1) for i in range(n)]
    a.sort()
    b = a[n // 2]
    print(sum([abs(x - b) for x in a]))

if __name__ == '__main__':
    main()