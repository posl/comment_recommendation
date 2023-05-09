def main():
    N = int(input())
    A = list(map(int,input().split()))
    while len(A) > 1:
        A.sort()
        A[0] %= A[-1]
        if A[0] == 0:
            A.pop(0)
    print(A[0])
