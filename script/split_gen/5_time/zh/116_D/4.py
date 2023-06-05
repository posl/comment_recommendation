def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append([t, d])
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    #print(sushi[:K])
    #print(sushi[K:])
    #print(set(sushi[:K]))
    #print(set(sushi[K:]))
    max_sushi = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i + j > N:
                break
            #print(i, j)
            #print(sushi[:i])
            #print(sushi[K-j:])
            tmp_sushi = sushi[:i] + sushi[K-j:]
            tmp_sushi.sort(key=lambda x: x[0])
            #print(tmp_sushi)
            cnt = 0
            tmp_sum = 0
            for k in range(K):
                cnt += 1
                tmp_sum += tmp_sushi[k][1]
                #print(tmp_sushi[k])
            #print(cnt)
            #print(tmp_sum)
            tmp_sum += cnt * cnt
            max_sushi = max(max_sushi, tmp_sum)
    print(max_sushi)
