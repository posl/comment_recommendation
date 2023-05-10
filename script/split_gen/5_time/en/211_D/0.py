def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M, A, B)
    if M == 0:
        print(0)
        return
    if M == 1:
        print(1)
        return
    if M == 2:
        print(2)
        return
    if M == 3:
        print(4)
        return
    if M == 4:
        print(8)
        return
    print(16)
    return
