def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) > 1:
        A.sort()
        A = [a - A[0] for a in A if a > A[0]]
    print(A[0])
