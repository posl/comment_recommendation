def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    assert len(A) == N
    assert 2 <= N <= 3 * 10 ** 5
    assert all(abs(x) <= 200 for x in A)
    print(sum((A[i] - A[j]) ** 2 for i in range(1, N) for j in range(i)))
