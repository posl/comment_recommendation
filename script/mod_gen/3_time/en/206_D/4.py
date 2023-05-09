def main():
    N = int(input())
    A = list(map(int, input().split()))
    I = 0
    J = N - 1
    ans = 0
    while I < J:
        if A[I] == A[J]:
            I += 1
            J -= 1
        elif A[I] < A[J]:
            I += 1
            A[I] += A[I - 1]
            ans += 1
        else:
            J -= 1
            A[J] += A[J + 1]
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()