def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(abs(A[0] + A[1]))
    elif N == 3:
        print(max(abs(A[0] + A[1] + A[2]), abs(A[0] - A[1] - A[2])))
    else:
        s = sum(A)
        if s > 0:
            tmp = 0
            for i in range(N):
                if i % 2 == 0:
                    tmp += A[i]
                else:
                    tmp -= A[i]
            print(abs(tmp))
        else:
            tmp = 0
            for i in range(N):
                if i % 2 == 0:
                    tmp -= A[i]
                else:
                    tmp += A[i]
            print(abs(tmp))
