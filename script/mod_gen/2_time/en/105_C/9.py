def main():
    # Write your code here
    n = int(input())
    if n == 0:
        print(0)
        return
    s = ''
    while n != 0:
        if n%2 == 0:
            s = s + '0'
            n = n//(-2)
        else:
            s = s + '1'
            n = n//(-2) + 1
    print(s[::-1])

if __name__ == '__main__':
    main()