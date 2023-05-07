def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #compute
    P = 0
    M = [0, 0, 0, 0]
    for i in range(N):
        M[0] += 1
        for j in range(4):
            if M[j] != 0:
                M[j] -= 1
                M[(j + A[i]) % 4] += 1
    for i in range(4):
        P += M[i] % 4
    #output
    print(P)
