def main():
    n = int(input())
    ans = ""
    while n > 0:
        if n % 2 == 0:
            ans = "B" + ans
            n = n // 2
        else:
            ans = "A" + ans
            n -= 1
    print(ans)

if __name__ == '__main__':
    main()