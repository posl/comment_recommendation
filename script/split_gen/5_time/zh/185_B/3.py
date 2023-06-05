def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    battery = N
    for i in range(M):
        if i == 0:
            battery -= A[i]
            if battery <= 0:
                print("No")
                return
            battery += B[i] - A[i]
            if battery >= N:
                battery = N
            if battery <= 0:
                print("No")
                return
        else:
            battery -= A[i] - B[i-1]
            if battery <= 0:
                print("No")
                return
            battery += B[i] - A[i]
            if battery >= N:
                battery = N
            if battery <= 0:
                print("No")
                return
    battery -= T - B[M-1]
    if battery <= 0:
        print("No")
        return
    print("Yes")
