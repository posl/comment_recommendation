def main():
    N = int(input())
    B = list(map(int,input().split()))
    A = []
    A.append(B[0])
    for i in range(1,N-1):
        if B[i] > B[i-1]:
            A.append(B[i-1])
        else:
            A.append(B[i])
    A.append(B[-1])
    print(sum(A))
