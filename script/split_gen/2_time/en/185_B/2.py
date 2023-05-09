def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    battery = N
    prev = 0
    for i in range(M):
        battery -= A[i] - prev
        if battery <= 0:
            print("No")
            exit()
        battery += B[i] - A[i]
        battery = min(battery, N)
        prev = B[i]
    battery -= T - prev
    if battery <= 0:
        print("No")
        exit()
    print("Yes")
