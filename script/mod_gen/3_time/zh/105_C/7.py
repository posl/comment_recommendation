def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append('0')
            n = n // (-2)
        else:
            ans.append('1')
            n = (n-1) // (-2)
    ans.reverse()
    print(''.join(ans))

if __name__ == '__main__':
    main()