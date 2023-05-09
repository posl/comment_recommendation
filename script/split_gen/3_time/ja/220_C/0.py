def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100
    sum = 0
    for i in range(100 * N):
        sum += B[i]
        if sum > X:
            print(i + 1)
            break
