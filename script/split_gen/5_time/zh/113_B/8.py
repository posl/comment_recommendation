def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 1000000
    min_index = 0
    for i in range(N):
        temp = T - H[i] * 0.006
        if abs(A - temp) < min_diff:
            min_diff = abs(A - temp)
            min_index = i + 1
    print(min_index)
