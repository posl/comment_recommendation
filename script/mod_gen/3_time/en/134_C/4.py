def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_a_count = a.count(max_a)
    if max_a_count == 1:
        for i in range(n):
            if a[i] == max_a:
                print(max(a[:i] + a[i + 1:]))
            else:
                print(max_a)
    else:
        for i in range(n):
            print(max_a)

if __name__ == '__main__':
    main()