def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = []
    for i in range(100):
        B.extend(A)
    print(B)
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            break
