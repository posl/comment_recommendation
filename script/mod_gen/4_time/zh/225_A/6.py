def main():
    s = input()
    n = len(s)
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    print(ans)

if __name__ == '__main__':
    main()