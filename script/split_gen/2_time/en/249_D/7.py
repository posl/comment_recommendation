def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if A[i] == A[j]:
                continue
            if A[i] % A[j] != 0:
                continue
            for k in range(1, N+1):
                if A[i] == A[k]:
                    continue
                if A[j] == A[k]:
                    continue
                if A[i] / A[j] == A[k]:
                    count += 1
    print(count//2)
