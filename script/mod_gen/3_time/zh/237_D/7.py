def main():
    n = int(input())
    s = input()
    l = 0
    r = n
    for i in range(n):
        if s[i] == 'L':
            r -= 1
        else:
            l += 1
    for i in range(l):
        print(i+1, end=' ')
    for i in range(r):
        print(l+r-i, end=' ')
    print()

if __name__ == '__main__':
    main()