def test():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        if i == 0:
            B[i] = A[i] - sum(B)
        else:
            B[i] = A[i] - B[i-1]
    print(" ".join(map(str, B)))

if __name__ == '__main__':
    test()