def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    num = 0
    for i in range(N):
        num += B.count(C[A[i]-1])
    print(num)
