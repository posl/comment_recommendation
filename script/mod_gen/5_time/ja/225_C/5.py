def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    ans = 'No'
    for i in range(1000000000):
        if i * 7 + 7 > n:
            break
        if b[0] == [i * 7 + 1, i * 7 + 2, i * 7 + 3, i * 7 + 4, i * 7 + 5, i * 7 + 6, i * 7 + 7]:
            ans = 'Yes'
            break
    print(ans)
main()

if __name__ == '__main__':
    main()