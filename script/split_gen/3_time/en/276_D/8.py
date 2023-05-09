def main():
    n = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        if A == [A[0]] * n:
            break
        for i in range(n):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
                count += 1
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
                count += 1
            else:
                count = -1
                break
    print(count)
