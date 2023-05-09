def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(N)]
    A.sort()
    b = A[N // 2]
    ans = sum([abs(A[i] - b) for i in range(N)])
    print(ans)
