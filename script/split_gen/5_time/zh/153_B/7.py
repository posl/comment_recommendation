def main():
    a = input().split()
    H = int(a[0])
    N = int(a[1])
    A = input().split()
    sumA = 0
    for i in range(N):
        sumA += int(A[i])
    if sumA >= H:
        print('Yes')
    else:
        print('No')
