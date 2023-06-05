def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_height = 0
    for i in range(n):
        if a[i] > max_height + 1:
            print(-1)
            return
        elif a[i] == max_height + 1:
            max_height += 1
    print(n - max_height)

if __name__ == '__main__':
    main()