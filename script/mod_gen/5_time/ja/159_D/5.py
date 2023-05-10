def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_set = set(A)
    A_len = len(A)
    ans = [0] * N
    for num in A_set:
        tmp = A.count(num)
        ans[num-1] = tmp * (tmp-1) // 2
    for i in range(A_len):
        print(ans[A[i]-1])

if __name__ == '__main__':
    main()