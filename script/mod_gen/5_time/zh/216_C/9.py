def main():
    n = int(input())
    ans = []
    while n > 0:
        if n & 1:
            ans.append('A')
            n -= 1
        else:
            ans.append('B')
            n //= 2
    print(''.join(ans[::-1]))

if __name__ == '__main__':
    main()