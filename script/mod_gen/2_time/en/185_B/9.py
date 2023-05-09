def problems185_b():
    N, M, T = map(int, input().split())
    battery = N
    prev = 0
    for i in range(M):
        A, B = map(int, input().split())
        battery -= (A - prev)
        if battery <= 0:
            return "No"
        battery += (B - A)
        if battery > N:
            battery = N
        prev = B
    battery -= (T - prev)
    if battery <= 0:
        return "No"
    return "Yes"

if __name__ == '__main__':
    problems185_b()