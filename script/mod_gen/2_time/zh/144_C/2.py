def main():
    N = int(input())
    ans = 0
    while N > 1:
        if N % 2 == 1:
            N -= 1
        else:
            N /= 2
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()