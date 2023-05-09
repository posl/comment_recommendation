def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            elif A[i] % 3 == 0:
                A[i] = A[i] / 3
            else:
                break
        else:
            cnt += 1
            continue
        break
    if len(set(A)) == 1:
        print(cnt)
    else:
        print(-1)
