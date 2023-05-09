def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print('Yes' if sum([A[i]*B[i] for i in range(N)]) == 0 else 'No')
