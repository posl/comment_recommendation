def main():
    N = int(input())
    books = list(map(int, input().split()))
    books.sort()
    ans = 0
    for i in range(N):
        if i + 1 < books[i]:
            ans = i
            break
        else:
            ans = i + 1
    print(ans)
main()

if __name__ == '__main__':
    main()