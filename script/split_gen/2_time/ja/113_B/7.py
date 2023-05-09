def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min = 100000000
    index = 1
    for i in range(N):
        temp = T - H[i] * 0.006
        if abs(A - temp) < min:
            min = abs(A - temp)
            index = i + 1
    print(index)
