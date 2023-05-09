def main():
    #n = int(input())
    #s = input()
    n = 6
    s = "abcbac"
    for i in range(1, n):
        l = 0
        while True:
            if i + l >= n:
                break
            if s[l] == s[i+l]:
                break
            l += 1
        print(l)

if __name__ == '__main__':
    main()