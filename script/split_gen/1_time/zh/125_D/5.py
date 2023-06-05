def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    min = 1000000000
    count = 0
    for i in range(N):
        sum += abs(A[i])
        if A[i] < 0:
            count += 1
        if abs(A[i]) < min:
            min = abs(A[i])
    if count % 2 == 0:
        print(sum)
    else:
        print(sum - min * 2)
