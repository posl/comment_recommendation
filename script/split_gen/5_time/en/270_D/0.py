def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    i = 0
    while A[i] < N:
        i += 1
    print(i+1)
