def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] == s[l + i]:
                break
            l += 1
        print(l)

if __name__ == '__main__':
    main()