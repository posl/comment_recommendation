def solve(N, A):
    count = 0
    while True:
        if all(a % 2 == 0 for a in A):
            count += 1
            A = [a / 2 for a in A]
        elif all(a % 3 == 0 for a in A):
            count += 1
            A = [a / 3 for a in A]
        elif all(a == A[0] for a in A):
            break
        else:
            return -1
    return count
N = int(raw_input())
A = map(int, raw_input().split())
print solve(N, A)
