def main():
    N = input()
    if N == '0':
        print('Yes')
        return
    if int(N[-1]) % 2 == 0:
        print('No')
        return
    ans = 0
    for i in range(len(N)):
        ans += int(N[i])
    if ans % 9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()