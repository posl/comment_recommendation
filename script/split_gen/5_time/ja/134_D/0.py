def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N, 0, -1):
        sum = 0
        for j in range(i, N+1, i):
            sum += b[j-1]
        if sum % 2 != a[i-1]:
            b[i-1] = 1
    M = sum(b)
    print(M)
    if M > 0:
        for i in range(N):
            if b[i] == 1:
                print(i+1, end=" ")
        print()
