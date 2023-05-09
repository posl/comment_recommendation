def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    second_max_a = sorted(a)[-2]
    for i in range(n):
        if a[i] == max_a:
            print(second_max_a)
        else:
            print(max_a)

if __name__ == '__main__':
    main()