def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] /= 2
            elif A[i] % 3 == 0:
                A[i] /= 3
            else:
                break
        else:
            count += 1
            continue
        break
    if A.count(A[0]) == N:
        print(count)
    else:
        print(-1)
