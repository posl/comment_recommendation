def main():
    S,T = map(str, input().split())
    A,B = map(int, input().split())
    U = str(input())
    if U == S:
        A = A - 1
    elif U == T:
        B = B - 1
    print(A,B)

if __name__ == '__main__':
    main()