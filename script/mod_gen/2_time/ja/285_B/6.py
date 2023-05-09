def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        for j in range(1, n-i):
            if s[j-1] != s[j+i-1]:
                l = j
        print(l)

if __name__ == '__main__':
    main()