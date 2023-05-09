def main():
    n = int(input())
    ans = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            ans.append('B')
        else:
            n -= 1
            ans.append('A')
    ans.reverse()
    print(''.join(ans))

if __name__ == '__main__':
    main()