def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            print("NO")
            exit()
    print("YES")
