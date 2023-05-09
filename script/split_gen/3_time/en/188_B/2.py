def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print('Yes')
    else:
        print('No')
