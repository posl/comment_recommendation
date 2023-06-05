def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0] * N
    count = 1
    for i in range(N):
        if A[i] == A[i + 1]:
            count += 1
        else:
            ans[A[i] - 1] = count
            count = 1
    for i in range(N):
        print(N - ans[i])
main()
