def main():
    H1, W1 = map(int, input().split(' '))
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split(' '))))
    H2, W2 = map(int, input().split(' '))
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split(' '))))
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if check(A, B, i, j, H2, W2):
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()