def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(set(A)) > 1:
        A.sort()
        A[-1] = A[-1] % A[-2]
        A = list(set(A))
    print(A[0])
