def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    book = 0
    for i in range(N):
        if a[i] <= book + 1:
            book += a[i]
        else:
            break
    print(book + 1)

if __name__ == '__main__':
    main()