def main():
    N, M = map(int, input().split())
    bridge = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        bridge[a] += 1
        bridge[b] += 1
    print(bridge.count(0))

if __name__ == '__main__':
    main()