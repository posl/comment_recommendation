def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    point = 0
    for i in range(N):
        point += B[A[i]-1]
        if i != N-1 and A[i] == A[i+1]-1:
            point += C[A[i]-1]
    print(point)
