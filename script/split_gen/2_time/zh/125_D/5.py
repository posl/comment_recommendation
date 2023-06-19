def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    if N == 2:
        if A[0] < 0 and A[1] < 0:
            print(-A[0]-A[1])
        elif A[0] < 0 and A[1] > 0:
            print(A[1]-A[0])
        else:
            print(A[0]+A[1])
        return
    elif N == 1:
        print(A[0])
        return
    else:
        count = 0
        for i in range(N):
            if A[i] < 0:
                count += 1
        if count % 2 == 0:
            print(sum([abs(i) for i in A]))
        else:
            print(sum([abs(i) for i in A]) - 2*min([abs(i) for i in A]))
