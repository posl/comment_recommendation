def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        #print(x)
        #print(A)
        #print(N)
        #print(bisect.bisect_left(A, x))
        print(N - bisect.bisect_left(A, x))
