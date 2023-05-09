def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    B = [A[0]]
    for i in range(1, N):
        B.append(B[i-1] + A[i])
    ans = 0
    for i in range(1, N):
        ans += A[i] * i - B[i-1]
    print(ans * 2)
