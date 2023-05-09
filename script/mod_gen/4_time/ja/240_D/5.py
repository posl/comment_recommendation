def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n):
        s.add(a[i])
        while True:
            if a[i] in s:
                a[i] += 1
            else:
                break
        print(a[i])

if __name__ == '__main__':
    main()