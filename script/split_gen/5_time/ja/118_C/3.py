def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) != 1:
        A.sort()
        x = A[0]
        y = A[1]
        if x == y:
            A = A[2:]
        else:
            A = A[2:] + [y-x]
    print(A[0])
