def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    if N == 1:
        print(0)
        exit()
    if A[0] != 1:
        A = [0] + A
    if A[-1] != N:
        A = A + [N+1]
    if N == 2:
        if M == 1:
            print(1)
        else:
            print(0)
        exit()
    max_d = 0
    d = []
    for i in range(M):
        d.append(A[i+1] - A[i] - 1)
        if d[-1] > max_d:
            max_d = d[-1]
    if max_d == 0:
        print(0)
        exit()
    if max_d == 1:
        print(1)
        exit()
    if max_d % 2 == 0:
        print(max_d//2)
    else:
        print(max_d//2 + 1)
main()
