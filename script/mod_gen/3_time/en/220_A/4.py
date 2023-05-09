def main():
    A, B, C = map(int, input().split())
    if A % C == 0:
        print(A)
    elif B % C == 0:
        print(B)
    elif A < C and B < C:
        print(-1)
    else:
        print(C * (B // C))

if __name__ == '__main__':
    main()