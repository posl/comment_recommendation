def main():
    S, T = map(str, input().split())
    A, B = map(int, input().split())
    U = str(input())
    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)

if __name__ == '__main__':
    main()