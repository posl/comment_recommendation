def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    for i in range(N):
        if A[i] != i+1:
            print("No")
            break
    else:
        print("Yes")
