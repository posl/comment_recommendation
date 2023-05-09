def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    cards = [0 for _ in range(M)]
    for a in A:
        cards[a] += 1
    for i in range(M):
        if cards[i] == 0:
            continue
        if cards[(i+1)%M] == 0:
            continue
        if cards[i] == 1 and cards[(i+1)%M] == 1:
            continue
        if cards[i] == 1:
            cards[i] -= 1
            cards[(i+1)%M] -= 1
            cards[(i+2)%M] += 1
        elif cards[(i+1)%M] == 1:
            cards[(i+1)%M] -= 1
            cards[(i+2)%M] -= 1
            cards[(i+3)%M] += 1
        else:
            cards[i] -= 2
            cards[(i+1)%M] -= 1
            cards[(i+2)%M] += 1
    ans = 0
    for i in range(M):
        if cards[i] == 0:
            continue
        if cards[i] == 1:
            ans += i
        else:
            ans += i*2
    print(ans)
