def main():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    if (C == 0 and A > B) or (C == 1 and A >= B):
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()