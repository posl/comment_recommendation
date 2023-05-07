def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edge = [list(map(int, input().split())) for _ in range(M)]
    edge.sort()
    print(edge)
