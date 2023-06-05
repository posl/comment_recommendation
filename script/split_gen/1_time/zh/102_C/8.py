def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = 0
    min = 10**9
    for i in range(-100, 101):
        b = i
        sum = 0
        for j in range(N):
            sum += abs(A[j] - (b+j+1))
        if sum < min:
            min = sum
    print(min)
