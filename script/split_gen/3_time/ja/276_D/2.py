def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 3 == 0:
                A[i] = A[i] // 3
                count += 1
            else:
                break
        else:
            continue
        break
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
                count += 1
            else:
                break
        else:
            continue
        break
    for i in range(N):
        if A[i] != A[0]:
            count = -1
            break
    print(count)
