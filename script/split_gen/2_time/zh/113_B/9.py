def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < min:
            min = abs(T - H[i] * 0.006 - A)
            index = i + 1
    print(index)
