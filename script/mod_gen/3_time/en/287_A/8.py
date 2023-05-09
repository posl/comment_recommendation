def main():
    N = int(input())
    if N == 1:
        print('Yes')
        return
    count = 0
    for i in range(N):
        if input() == 'For':
            count += 1
    if count > N // 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()