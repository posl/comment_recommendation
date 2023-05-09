def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    ans = 0
    for i in range(N):
        if i%2 == 0:
            B[i] = A[i]
        else:
            B[i] = -A[i]
    ans = sum(B)
    print(ans)
