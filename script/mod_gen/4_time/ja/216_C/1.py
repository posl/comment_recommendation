def main():
    N = int(input())
    ans = []
    while N > 0:
        if N % 2 == 0:
            N //= 2
            ans.append('B')
        else:
            N -= 1
            ans.append('A')
    print(''.join(ans[::-1]))

if __name__ == '__main__':
    main()