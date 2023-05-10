def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    count = 0
    for i in range(N):
        if A[i] <= B[i]:
            count += A[i]
            if A[i+1] <= B[i] - A[i]:
                count += A[i+1]
                A[i+1] = 0
            else:
                count += B[i] - A[i]
                A[i+1] -= B[i] - A[i]
        else:
            count += B[i]
    print(count)
