def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [x-1 for x in P]
    count = 0
    for i in range(N):
        if P[i] == i:
            count += 1
            if i+1 < N:
                P[i], P[i+1] = P[i+1], P[i]
            else:
                P[i], P[0] = P[0], P[i]
    print(count)
