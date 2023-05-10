def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = list(range(n))
    for i in range(n):
        if a[i] != b[i]:
            print(b[i])
            return
    print(b[-1] + 1)

if __name__ == '__main__':
    main()