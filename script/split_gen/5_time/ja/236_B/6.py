def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[int(len(A)/2)])
