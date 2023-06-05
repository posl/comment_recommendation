def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i] > i:
            print(i)
            return
    print(N)
