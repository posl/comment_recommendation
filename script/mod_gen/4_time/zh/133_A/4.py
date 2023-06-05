def main():
    N,A,B = map(int, input().split())
    if N*A < B:
        print(N*A)
    else:
        print(B)

if __name__ == '__main__':
    main()