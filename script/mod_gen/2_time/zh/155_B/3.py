def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                continue
            else:
                print('DENIED')
                return
    print('APPROVED')
    return

if __name__ == '__main__':
    main()