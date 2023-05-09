def main():
    N = input()
    N = N[::-1]
    N = [int(i) for i in N]
    if sum(N)%9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()