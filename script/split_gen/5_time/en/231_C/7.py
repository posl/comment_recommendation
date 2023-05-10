def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for i in range(Q)]
    A.sort()
    A.append(10**10)
    for x in X:
        for i in range(N):
            if A[i] >= x:
                print(N-i)
                break
