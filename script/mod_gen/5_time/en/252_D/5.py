def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N-2):
        if A[i] == A[i+1]:
            continue
        for j in range(i+1, N-1):
            if A[j] == A[j+1]:
                continue
            if A[i] + A[j] <= A[-1]:
                cnt += 1
            else:
                break
    print(cnt)

if __name__ == '__main__':
    main()