def main():
    N = int(input())
    flag = False
    for i in range(1,10):
        if N % i == 0 and 1 <= N // i <= 9:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()