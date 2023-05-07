def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(360)
    A.append(0)
    A = sorted(A)
    #print(A)
    max = 0
    for i in range(N+1):
        if A[i+1]-A[i] > max:
            max = A[i+1]-A[i]
    print(360-max)
