def main():
    A = list(map(int, input().split()))
    A.sort()
    print(abs(A[1]-A[0])+abs(A[2]-A[1]))
