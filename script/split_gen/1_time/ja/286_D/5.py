def main():
    N, X = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(2**N):
        total = 0
        for j in range(N):
            if (i>>j)&1:
                total += A[j]*B[j]
        if total == X:
            print("Yes")
            return
    print("No")
    return
