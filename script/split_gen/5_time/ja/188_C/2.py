def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [[i, A[i]] for i in range(len(A))]
    while len(A) > 2:
        A = [max(A[i], A[i+1]) for i in range(0, len(A), 2)]
    print(min(A[0][0], A[1][0]) + 1)
