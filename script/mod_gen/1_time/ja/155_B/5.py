def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in A:
        if i % 2 == 0:
            if i % 3 == 0 or i % 5 == 0:
                pass
            else:
                print('DENIED')
                exit()
    print('APPROVED')

if __name__ == '__main__':
    main()