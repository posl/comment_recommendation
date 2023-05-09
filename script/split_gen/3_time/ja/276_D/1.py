def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                count = -1
                break
        if count == -1:
            break
        count += 1
        if all([A[0] == A[i] for i in range(1, N)]):
            break
    print(count)
