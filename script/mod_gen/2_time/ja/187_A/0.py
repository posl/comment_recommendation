def main():
    A, B = map(int, input().split())
    A = sum(int(i) for i in str(A))
    B = sum(int(i) for i in str(B))
    if A > B:
        print(A)
    else:
        print(B)

if __name__ == '__main__':
    main()