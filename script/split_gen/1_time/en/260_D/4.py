def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    cards = [0] * N
    for i in range(N):
        cards[P[i] - 1] = i
    eaten = [0] * N
    for i in range(N):
        eaten[i] = -1
    for i in range(N):
        if eaten[i] != -1:
            continue
        eaten[i] = i
        j = cards[i]
        for k in range(K - 1):
            if j + 1 >= N:
                break
            j += 1
            if eaten[j] != -1:
                break
            eaten[j] = i
    for i in range(N):
        print(eaten[i] + 1)
main()
