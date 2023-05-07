def main():
    N = int(input())
    ans = ''
    while N > 0:
        N -= 1
        ans = chr(ord('a') + N % 26) + ans
        N //= 26
    print(ans)
main()

if __name__ == '__main__':
    main()