def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 1:
                print(cnt)
                return
            else:
                A[i] = A[i] // 2
        cnt += 1
