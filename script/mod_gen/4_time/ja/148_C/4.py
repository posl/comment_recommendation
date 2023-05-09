def main():
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    for i in range(B, (A*B)+1):
        if i % A == 0 and i % B == 0:
            print(i)
            break

if __name__ == '__main__':
    main()