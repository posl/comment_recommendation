def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        cnt += B[i] - A[i] + 1
    print(cnt)
