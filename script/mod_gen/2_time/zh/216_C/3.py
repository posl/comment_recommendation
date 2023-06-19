def main():
    N = int(input())
    ans = ""
    while N != 0:
        if N % 2 == 0:
            N = N // 2
            ans += "B"
        else:
            N -= 1
            ans += "A"
    print(ans[::-1])

if __name__ == '__main__':
    main()