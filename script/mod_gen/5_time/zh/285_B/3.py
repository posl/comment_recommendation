def main():
    n = int(input())
    s = input()
    for i in range(n-1):
        l = 0
        while i + l < n and i + l * 2 < n and s[i] != s[i + l] and s[i + l] != s[i + l * 2]:
            l += 1
        print(l)

if __name__ == '__main__':
    main()