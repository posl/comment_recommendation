def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    if N == 2:
        if x == A[0] and y == 0:
            print("Yes")
        else:
            print("No")
    elif N == 3:
        if x == A[0] + A[1] and y == A[2]:
            print("Yes")
        else:
            print("No")
    else:
        if x == A[0] + A[1] and y == A[2]:
            print("Yes")
        elif x == A[0] + A[1] + A[3] and y == A[2] + A[4]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()