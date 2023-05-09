def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0] * N
    cnt = 1
    for i in range(N):
        if A[i] != A[i+1]:
            ans[cnt-1] += 1
            cnt = 1
        else:
            cnt += 1
    print(*ans, sep="\n")

if __name__ == '__main__':
    main()