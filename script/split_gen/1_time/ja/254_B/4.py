def main():
    N = int(input())
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                print(1,end=' ')
            else:
                print(A[i-1][j-1]+A[i-1][j],end=' ')
        print()
        A.append([1]*(i+1))
