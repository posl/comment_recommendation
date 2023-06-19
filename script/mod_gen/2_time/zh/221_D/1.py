def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dict = {}
    for i in range(N):
        for j in range(A[i], A[i] + B[i]):
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
    ans = [0] * N
    for i in dict.values():
        ans[i - 1] += 1
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()