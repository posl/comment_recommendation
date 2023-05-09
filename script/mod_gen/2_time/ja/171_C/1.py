def main():
    n = int(input())
    ans = []
    while n > 0:
        n -= 1
        ans.append(chr(ord('a') + n % 26))
        n //= 26
    print("".join(ans[::-1]))

if __name__ == '__main__':
    main()