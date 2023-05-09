def main():
    N, M = map(int, input().split())
    if M == 0:
        print('Yes')
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    CD.sort()
    for P in permutations(range(1, N+1)):
        for ab in AB:
            if ab not in [(P[ab[0]-1], P[ab[1]-1]), (P[ab[1]-1], P[ab[0]-1])]:
                break
        else:
            print('Yes')
            return
    print('No')
