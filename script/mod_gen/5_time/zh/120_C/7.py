def main():
    n = int(input())
    s = input()
    r = 0
    b = 0
    for i in range(n):
        if s[i] == '0':
            r += 1
        else:
            b += 1
    print(n - abs(r - b))

if __name__ == '__main__':
    main()