def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    X = int(input())
    sumA = sum(A)
    sumB = sumA * (X // sumA)
    i = N * (X // sumA)
    while sumB <= X:
        sumB += A[i % N]
        i += 1
    print(i)
