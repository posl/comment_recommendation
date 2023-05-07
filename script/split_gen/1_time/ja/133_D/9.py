def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(A[0])
    if N == 3:
        print(A[0]+A[1]-A[2], A[1]+A[2]-A[3], A[2]+A[3]-A[0])
    else:
        B = [0]*N
        for i in range(N):
            B[i] = (A[i]+A[i+1])//2
        print(*B)
main()
