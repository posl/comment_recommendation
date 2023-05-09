def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) > 1:
        A.sort()
        A[-1] %= A[0]
        if A[-1] == 0:
            A.pop()
    print(A[0])
