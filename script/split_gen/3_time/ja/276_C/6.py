def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = []
    for i in range(N):
        Q.append(i+1)
    cnt = 0
    while P != Q:
        for i in range(N-1):
            if Q[i] > Q[i+1]:
                Q[i], Q[i+1] = Q[i+1], Q[i]
                cnt += 1
    print(cnt)
