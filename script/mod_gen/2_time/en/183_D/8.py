def main():
    N, W = map(int, input().split())
    # N: Number of people
    # W: Water heater capacity
    # S_i: Start time
    # T_i: End time
    # P_i: Water usage
    # T: Total water usage
    T = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        T[S] += P
        T[T] -= P
    for i in range(200000):
        T[i + 1] += T[i]
    for i in range(200000):
        if T[i] > W:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()