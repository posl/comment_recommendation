def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [A[i]-(i+1) for i in range(N)]
    B.sort()
    if N%2 == 1:
        b = B[int(N/2)]
    else:
        b = (B[int(N/2)] + B[int(N/2-1)])/2
    print(int(sum([abs(A[i]-(b+(i+1))) for i in range(N)])))
