def main():
    #input
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    
    #output
    for i in range(1, N+1):
        d = 0
        for j in range(M):
            if i in AB[j]:
                d += 1
        print(d, *sorted([a for a, b in AB if i == a] + [b for a, b in AB if i == b]))
