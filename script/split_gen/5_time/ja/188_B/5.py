def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    for i in range(N):
        result += A[i] * B[i]
    if result == 0:
        print("Yes")
    else:
        print("No")
