def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    diff = 10**9
    i, j = 0, 0
    while i < N and j < M:
        diff = min(diff, abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(diff)
main()
As you can see, the main idea is to sort the list A and B and then compare the minimum difference of A[i] and B[j] for all i and j. The code is written in Python, but it also works in PyPy.
This problem is from the AtCoder Beginner Contest 212.
