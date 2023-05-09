def main():
    N = int(input())
    N -= 1
    ans = ""
    while N >= 0:
        ans = chr(ord('a') + (N % 26)) + ans
        N //= 26
        N -= 1
    print(ans)

if __name__ == '__main__':
    main()