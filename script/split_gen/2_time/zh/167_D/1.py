def main():
    N,K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    count = 0
    i = 0
    while count < K:
        count += 1
        i = A[i] - 1
        if i == 0:
            break
    print(A[i])
