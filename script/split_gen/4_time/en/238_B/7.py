def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [360 - i for i in A]
    A = A[::-1]
    A.append(0)
    A = [A[i] - A[i+1] for i in range(N)]
    A = [i if i > 0 else i + 360 for i in A]
    print(360 - max(A))
