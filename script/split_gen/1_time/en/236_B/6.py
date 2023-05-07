def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #process
    A.sort()
    for i in range(N):
        if A[2*i]!=A[2*i+1]:
            print(A[2*i])
            break
