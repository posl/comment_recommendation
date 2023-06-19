def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(N):
        temperature = T - H[i] * 0.006
        if abs(A - temperature) < min:
            min = abs(A - temperature)
            index = i + 1
    print(index)
