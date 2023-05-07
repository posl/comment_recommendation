def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(A)
    #print(N, M)
    count = 0
    while N > 0:
        N -= A[count]
        count += 1
    print(A[count-1])
