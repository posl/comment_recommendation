def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    AB = [B[0]-A[0], B[1]-A[1]]
    BC = [C[0]-B[0], C[1]-B[1]]
    CD = [D[0]-C[0], D[1]-C[1]]
    DA = [A[0]-D[0], A[1]-D[1]]
    if (AB[0]*BC[1]-AB[1]*BC[0])*(CD[0]*DA[1]-CD[1]*DA[0])<0:
        print('No')
    else:
        print('Yes')
