def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N):
        result += 1/A[i]
    print(1/result)
