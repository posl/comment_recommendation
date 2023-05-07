def main():
    N = int(input())
    A = list(map(int, input().split()))
    print("N =", N)
    print("A =", A)
    print("")
    # convert A to a list of 2s and 3s
    B = []
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
            B.append(2)
        while A[i] % 3 == 0:
            A[i] = A[i] // 3
            B.append(3)
    print("B =", B)
    print("")
    # check if all elements of A are equal
    for i in range(N-1):
        if A[i] != A[i+1]:
            print(-1)
            return
    # count the number of 2s and 3s in B
    count2 = 0
    count3 = 0
    for i in range(len(B)):
        if B[i] == 2:
            count2 += 1
        if B[i] == 3:
            count3 += 1
    print("count2 =", count2)
    print("count3 =", count3)
    print("")
    # find the minimum number of operations
    print(min(count2, count3) + abs(count2 - count3))
