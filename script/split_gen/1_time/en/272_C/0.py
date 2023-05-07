def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if len(A) == 2:
        if (A[0] + A[1]) % 2 == 0:
            print(A[0] + A[1])
        else:
            print(-1)
    else:
        for i in range(1, len(A)):
            if (A[i] + A[i-1]) % 2 == 0:
                print(A[i] + A[i-1])
                break
        else:
            print(-1)
