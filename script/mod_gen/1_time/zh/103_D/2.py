def main():
    N, M = map(int, input().split())
    bridge = [0] * N
    for i in range(N):
        bridge[i] = i
    for i in range(M):
        a, b = map(int, input().split())
        bridge[a - 1] = min(bridge[a - 1], bridge[b - 1])
        bridge[b - 1] = min(bridge[a - 1], bridge[b - 1])
    print(len(set(bridge)) - 1)

if __name__ == '__main__':
    main()