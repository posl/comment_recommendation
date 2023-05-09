def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_even = A[::2]
    A_odd = A[1::2]
    if sum(A_even) + sum(A_odd) - sum(A_odd) >= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()