def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_index = a.index(max_a)
    for i in range(n):
        if i == max_index:
            print(max(a[:i] + a[i+1:]))
        else:
            print(max_a)

if __name__ == '__main__':
    main()