def run():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    blocks = [0] * 4
    for a in A:
        blocks[0] += 1
        blocks[a] += 1
        P += blocks[a - 1]
        blocks[a - 1] = 0
    print(P)
