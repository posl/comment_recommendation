def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    if N % 2 == 0:
        #print("even")
        print(sum(A[N//2:]) - sum(A[:N//2]))
    else:
        #print("odd")
        print(sum(A[N//2+1:]) - sum(A[:N//2]))
