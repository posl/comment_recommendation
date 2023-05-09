def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
    else:
        for i in range(N-1):
            if A[i] % 2 == 0:
                print(A[i])
                break
        else:
            print(-1)
