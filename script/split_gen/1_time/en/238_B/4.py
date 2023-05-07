def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [360 - a for a in A]
    A = [A[i] - A[i + 1] for i in range(N - 1)]
    A.append(360 - A[-1])
    print(sum(A) // 2)
