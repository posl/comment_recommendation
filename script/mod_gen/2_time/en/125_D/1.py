def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A[0], A[1]))
        return
    if N == 3:
        print(max(A[0] + A[1], A[0] + A[2], A[1] + A[2]))
        return
    # N >= 4
    B = [0] * (N - 1)
    for i in range(N - 1):
        B[i] = A[i] + A[i + 1]
    # print(B)
    if N % 2 == 0:
        # even
        # print("even")
        B_even = B[::2]
        B_odd = B[1::2]
        B_even.sort(reverse=True)
        B_odd.sort(reverse=True)
        # print(B_even)
        # print(B_odd)
        if B_even[0] < 0:
            print(sum(B))
            return
        if B_odd[0] < 0:
            print(sum(B))
            return
        print(sum(B_even) + sum(B_odd))
        return
    else:
        # odd
        # print("odd")
        B_even = B[::2]
        B_odd = B[1::2]
        B_even.sort(reverse=True)
        B_odd.sort(reverse=True)
        # print(B_even)
        # print(B_odd)
        if B_even[0] < 0:
            print(sum(B))
            return
        if B_odd[0] < 0:
            print(sum(B))
            return
        print(sum(B_even) + sum(B_odd) - B[-1])
        return
main()

if __name__ == '__main__':
    main()