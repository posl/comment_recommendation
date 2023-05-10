def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    vote = 0
    for i in range(N):
        vote += A[i] + B[i]
    vote /= 2
    vote = int(vote)
    aoki = 0
    for i in range(N):
        aoki += A[i]
        if aoki >= vote:
            print(i+1)
            break
