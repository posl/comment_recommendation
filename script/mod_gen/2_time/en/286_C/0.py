def main():
    n, a, b = map(int, input().split())
    s = input()
    count = 0
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            count += 1
    if count == 0:
        print(0)
    elif count == 1:
        print(a)
    elif count == 2:
        print(min(a,b)*2)
    else:
        print((count-1)*b+a)

if __name__ == '__main__':
    main()