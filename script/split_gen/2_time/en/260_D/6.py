def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [i - 1 for i in P]
    eaten = [-1] * N
    for i in range(N):
        if eaten[i] != -1:
            continue
        eaten[i] = i
        j = i
        while True:
            j = P[j]
            if eaten[j] != -1:
                break
            eaten[j] = i
    for i in range(N):
        if eaten[i] == -1:
            continue
        j = i
        while True:
            j = P[j]
            if eaten[j] == i:
                break
            eaten[j] = i
    for i in range(N):
        print(eaten[i] + 1)
