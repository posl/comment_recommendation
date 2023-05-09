def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
            cnt += 1
    print(cnt)
