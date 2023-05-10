def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    count = 0
    if sumA > X:
        while sumA <= X:
            count += 1
            sumA += A[count%N]
    else:
        count = (X//sumA)*N
        sumA = (X//sumA)*sumA
        while sumA <= X:
            count += 1
            sumA += A[count%N]
    print(count)
