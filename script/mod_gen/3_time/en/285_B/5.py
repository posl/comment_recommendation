def main():
    n = int(input())
    s = input()
    for i in range(n):
        l = 0
        while True:
            if i + l >= n:
                break
            if s[i] != s[i+l]:
                l += 1
            else:
                break
        print(l)

if __name__ == '__main__':
    main()