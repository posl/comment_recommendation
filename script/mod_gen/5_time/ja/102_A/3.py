def main():
    n = int(input())
    ans = 0
    for i in range(1, 10**9):
        if i % 2 == 0 and i % n == 0:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()