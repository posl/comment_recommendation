def main():
    N, M = map(int, input().split())
    #print(N, M)
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    #print(AB)
    count = 0
    for a in range(1, N):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                #print(a, b, c)
                if [a, b] in AB and [b, c] in AB and [c, a] in AB:
                    count += 1
    print(count)
