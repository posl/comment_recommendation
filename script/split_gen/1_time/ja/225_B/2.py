def main():
    N = int(input())
    A = [0 for i in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        A[a-1] += 1
        A[b-1] += 1
    if A.count(1) == 1 and A.count(N-1) == 1:
        print("Yes")
    else:
        print("No")
