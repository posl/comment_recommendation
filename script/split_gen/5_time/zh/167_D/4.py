def main():
    [N,K] = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    count = 0
    while count < K:
        count += 1
        A = [A[ai-1] for ai in A]
    print(A[0])
