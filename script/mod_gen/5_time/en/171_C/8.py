def main():
    n = int(input().strip())
    #print(n)
    #print(26*26*26*26*26)
    #print(26*26*26*26)
    #print(26*26*26)
    #print(26*26)
    #print(26)
    n -= 1
    ans = ""
    while True:
        ans = chr(ord('a') + n % 26) + ans
        n = n // 26
        if n == 0:
            break
        n -= 1
    print(ans)

if __name__ == '__main__':
    main()