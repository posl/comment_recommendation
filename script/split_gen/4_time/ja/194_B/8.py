def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    min_A = min(A)
    min_B = min(B)
    if A.index(min_A) == B.index(min_B):
        if min_A < min_B:
            min_B = sorted(B)[1]
        else:
            min_A = sorted(A)[1]
    print(min(min_A,min_B))
