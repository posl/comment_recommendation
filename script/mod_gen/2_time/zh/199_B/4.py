def square():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    if A ** 2 + B ** 2 < C ** 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    square()