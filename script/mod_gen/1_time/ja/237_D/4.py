def main():
    n = int(input())
    s = input()
    a = [0] * (n+1)
    l = 0
    r = n
    for i in range(n):
        if s[i] == 'L':
            a[r] = i+1
            r -= 1
        else:
            a[l] = i+1
            l += 1
    print(*a)

if __name__ == '__main__':
    main()