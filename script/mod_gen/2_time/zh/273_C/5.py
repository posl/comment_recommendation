def main():
    n = int(input())
    A = list(map(int, input().split()))
    A_set = set(A)
    A.sort()
    A_dict = {}
    for i in range(n):
        A_dict[A[i]] = i
    for i in range(n):
        cnt = 0
        for j in range(A_dict[A[i]]):
            if A[j] > A[i]:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()