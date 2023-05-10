def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append([d, t])
    sushi.sort(reverse=True)
    #print(sushi)
    #print(sushi[:K])
    #print(sushi[K:])
    #print(sushi[K-1][0])
    #print(sushi[K-1][1])
    #print(sushi[K-1][0] * sushi[K-1][1])
    #print(sushi[K-1][1] * sushi[K-1][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1] + sushi[K][1] * sushi[K][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1] + sushi[K][1] * sushi[K][1] - sushi[K+1][0] * sushi[K+1][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1] + sushi[K][1] * sushi[K][1] - sushi[K+1][0] * sushi[K+1][1] + sushi[K+1][1] * sushi[K+1][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1] + sushi[K][1] * sushi[K][1] - sushi
