def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += A[i] * B[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")
