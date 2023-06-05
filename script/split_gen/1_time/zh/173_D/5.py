def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(A[0])
    A.append(A[1])
    A.append(A[2])
    max = 0
    for i in range(1, N+1):
        sum = 0
        if i == 1:
            sum = A[i-1] + A[i+1]
            if sum > max:
                max = sum
        elif i == N:
            sum = A[i-1] + A[i+1]
            if sum > max:
                max = sum
        else:
            sum = A[i-1] + A[i+1]
            if sum > max:
                max = sum
    print(max)
