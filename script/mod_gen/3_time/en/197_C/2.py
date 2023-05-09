def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        return
    if N == 2:
        print(A[0] ^ A[1])
        return
    if N == 3:
        print(A[0] ^ A[1] ^ A[2])
        return
    # N >= 4
    # 1. Get the first number
    # 2. Get the last number
    # 3. Get the middle numbers
    # 4. If there is only one number in the middle, get that
    # 5. If there is more than one number in the middle, get the XOR of all of them
    # 6. XOR all of the first, middle and last numbers
    first = A[0]
    last = A[N - 1]
    middle = A[1:N - 1]
    if len(middle) == 1:
        middle = middle[0]
    else:
        middle = reduce(lambda x, y: x ^ y, middle)
    print(first ^ middle ^ last)

if __name__ == '__main__':
    solve()