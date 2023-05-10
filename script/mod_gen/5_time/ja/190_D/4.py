def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i * (i + 1) // 2 >= n:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()