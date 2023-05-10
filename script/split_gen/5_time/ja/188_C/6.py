def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [[A[i], i+1] for i in range(2**N)]
    while len(A) > 2:
        A = [[max(A[2*i-1][0], A[2*i][0]), A[2*i-1][1]] for i in range(1, len(A)//2+1)]
    A = sorted(A, key=lambda x: x[0])
    print(A[0][1])
