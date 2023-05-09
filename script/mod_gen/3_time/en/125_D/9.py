def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    if N == 2:
        print(sum(A))
        return
    if N == 3:
        print(max(sum(A), sum([-A[0], A[1], -A[2]]), sum([-A[0], -A[1], A[2]])))
        return
    if N == 4:
        print(max(sum(A), sum([-A[0], A[1], -A[2], A[3]]), sum([-A[0], -A[1], A[2], -A[3]])))
        return
    if N == 5:
        print(max(sum(A), sum([-A[0], A[1], -A[2], A[3], -A[4]]), sum([-A[0], -A[1], A[2], -A[3], A[4]])))
        return
    if N == 6:
        print(max(sum(A), sum([-A[0], A[1], -A[2], A[3], -A[4], A[5]]), sum([-A[0], -A[1], A[2], -A[3], A[4], -A[5]])))
        return
    if N == 7:
        print(max(sum(A), sum([-A[0], A[1], -A[2], A[3], -A[4], A[5], -A[6]]), sum([-A[0], -A[1], A[2], -A[3], A[4], -A[5], A[6]])))
        return
    if N == 8:
        print(max(sum(A), sum([-A[0], A[1], -A[2], A[3], -A[4], A[5], -A[6], A[7]]), sum([-A[0], -A[1], A[2], -A[3], A[4], -A[5], A[6], -A[7]])))
        return
    if N == 9:
        print(max(sum(A), sum([-A[0], A[1], -A[2], A[3], -A[4

if __name__ == '__main__':
    main()