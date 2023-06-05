def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    for i in range(n):
        if a[i] != max_a:
            print(max_a)
        else:
            print(sorted(a[:-1])[-1])

if __name__ == '__main__':
    main()