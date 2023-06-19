def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append((i+1, A[i]))
    B.sort(key=lambda x:x[1])
    for i in range(N):
        print(B[i][0], end=" ")
    print()
