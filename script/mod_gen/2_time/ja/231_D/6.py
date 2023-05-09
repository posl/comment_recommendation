def main():
    N, M = map(int, input().split())
    for i in range(M):
        A, B = map(int, input().split())
        if A == 1:
            if B == N:
                print('No')
                return
        elif A == N:
            if B == 1:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()