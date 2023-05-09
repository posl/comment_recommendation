def main():
    #input
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    #output
    for i in range(N):
        print("Yes" if K-Q+A.count(i+1)>0 else "No")
