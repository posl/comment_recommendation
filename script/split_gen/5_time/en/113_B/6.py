def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    closest = 100000000
    closest_index = 0
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < closest:
            closest = diff
            closest_index = i + 1
    print(closest_index)
