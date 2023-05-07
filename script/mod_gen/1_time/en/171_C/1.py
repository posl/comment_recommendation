def main():
    N = int(input())
    ans = ""
    while N > 0:
        N -= 1
        ans = chr(N % 26 + ord('a')) + ans
        N //= 26
    print(ans)

if __name__ == '__main__':
    main()