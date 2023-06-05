def main():
    N, M = [int(x) for x in input().split()]
    if M == 0:
        print(1)
        return
    A = [int(x) for x in input().split()]
    A.sort()
    if A[0] != 1:
        A = [0] + A
    if A[-1] != N:
        A = A + [N+1]
    #print(A)
    k = 1
    while True:
        for i in range(0, len(A)-1):
            if A[i+1] - A[i] - 1 < k:
                break
        else:
            print(k)
            return
        k += 1
main()
