def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        for j in range(B[i] + 1):
            if A[i] * j == X:
                print('Yes')
                exit()
            for k in range(N):
                if i == k:
                    continue
                for l in range(B[k] + 1):
                    if A[i] * j + A[k] * l == X:
                        print('Yes')
                        exit()
    print('No')
