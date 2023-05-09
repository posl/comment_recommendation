def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append([A[i], i+1])
    B.sort()
    for i in range(N):
        print(B[i][1], end=" ")
    print()
