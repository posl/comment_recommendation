def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i] != A[j]:
                count += 1
    print(count)
