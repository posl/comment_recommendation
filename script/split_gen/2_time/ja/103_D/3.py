def main():
    N, M = map(int, input().split())
    bridge = [0] * M
    for i in range(M):
        bridge[i] = list(map(int, input().split()))
    bridge.sort(key=lambda x: x[1])
    cnt = 0
    while len(bridge) > 0:
        cnt += 1
        bridge = [x for x in bridge if x[0] < bridge[0][1] and x[1] > bridge[0][1]]
    print(cnt)
