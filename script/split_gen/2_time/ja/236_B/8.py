def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    B = []
    for i in range(1,N+1):
        B.append(A.count(i))
    #print(B)
    for i in range(len(B)):
        if B[i] == 1:
            print(i+1)
