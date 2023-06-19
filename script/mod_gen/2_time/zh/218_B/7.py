def main():
    p = list(map(int, input().split()))
    s = [None] * 26
    for i in range(26):
        s[i] = chr(ord('a') + p[i] - 1)
    print("".join(s))

if __name__ == '__main__':
    main()