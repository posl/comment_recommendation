def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] - A[j] == 0:
                count += 1
    print(count)
