def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] != s[i + l]:
                l += 1
            else:
                break
        print(l)
    return

if __name__ == '__main__':
    main()