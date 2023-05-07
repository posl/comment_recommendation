def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        if len(set(A)) == 1:
            print(cnt)
            break
        for i in range(N):
            if A[i] % 3 == 0:
                A[i] = A[i] // 3
                cnt += 1
                break
            elif A[i] % 2 == 0:
                A[i] = A[i] // 2
                cnt += 1
                break
        else:
            print(-1)
            break
