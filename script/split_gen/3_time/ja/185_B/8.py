def main():
    N, M, T = map(int, input().split())
    AB = [tuple(map(int, input().split())) for i in range(M)]
    battery = N
    time = 0
    for a, b in AB:
        battery -= a - time
        if battery <= 0:
            print('No')
            return
        battery = min(N, battery + b - a)
        time = b
    battery -= T - time
    if battery <= 0:
        print('No')
        return
    print('Yes')
