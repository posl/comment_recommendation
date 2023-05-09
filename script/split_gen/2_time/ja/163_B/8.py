def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    sumA = sum(A)
    if sumA > N:
        print(-1)
    else:
        print(N-sumA)
