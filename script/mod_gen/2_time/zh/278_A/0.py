def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if A[0]==0:
        print(0)
        return
    if N==1:
        print(A[0])
        return
    if A[1]==0:
        print(1)
        return
    if N==2:
        print(A[0]+A[1])
        return
    if A[2]==0:
        print(2)
        return
    if N==3:
        print(A[0]+A[1]+A[2])
        return
    if A[3]==0:
        print(3)
        return
    if N==4:
        print(A[0]+A[1]+A[2]+A[3])
        return
    if A[4]==0:
        print(4)
        return
    if N==5:
        print(A[0]+A[1]+A[2]+A[3]+A[4])
        return
    if A[5]==0:
        print(5)
        return
    if N==6:
        print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5])
        return
    if A[6]==0:
        print(6)
        return
    if N==7:
        print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6])
        return
    if A[7]==0:
        print(7)
        return
    if N==8:
        print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7])
        return
    if A[8]==0:
        print(8)
        return
    if N==9:
        print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8])
        return
    if A[9]==0:
        print(9)
        return
    if N==10:
        print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6

if __name__ == '__main__':
    solve()