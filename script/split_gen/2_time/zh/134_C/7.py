def main():
    N=int(input())
    A=[]
    for i in range(N):
        A.append(int(input()))
    for i in range(N):
        A_copy=A.copy()
        A_copy.remove(A[i])
        print(max(A_copy))
main()
