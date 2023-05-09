def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    if (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])<0:
        print("No")
    elif (C[0]-B[0])*(D[1]-C[1])-(C[1]-B[1])*(D[0]-C[0])<0:
        print("No")
    elif (D[0]-C[0])*(A[1]-D[1])-(D[1]-C[1])*(A[0]-D[0])<0:
        print("No")
    elif (A[0]-D[0])*(B[1]-A[1])-(A[1]-D[1])*(B[0]-A[0])<0:
        print("No")
    else:
        print("Yes")
