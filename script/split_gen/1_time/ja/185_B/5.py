def main():
    N, M, T = map(int, input().split())
    battery = N
    time = 0
    for i in range(M):
        A, B = map(int, input().split())
        battery -= A - time
        if battery <= 0:
            print("No")
            return
        battery += B - A
        battery = min(battery, N)
        time = B
    battery -= T - time
    if battery <= 0:
        print("No")
    else:
        print("Yes")
