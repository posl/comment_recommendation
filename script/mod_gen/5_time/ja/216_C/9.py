def main():
    N = int(input())
    ans = []
    while N > 0:
        if N % 2 == 1:
            N -= 1
            ans.append('A')
        else:
            N //= 2
            ans.append('B')
    ans.reverse()
    print(''.join(ans))

if __name__ == '__main__':
    main()