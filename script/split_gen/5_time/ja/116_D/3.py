def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    t = []
    d = []
    for i in range(N):
        t.append(sushi[i][0])
        d.append(sushi[i][1])
    t = t[:K]
    d = d[:K]
    t.sort()
    d.sort()
    d.reverse()
    t_set = set(t)
    t_set = list(t_set)
    t_set.sort()
    t_set.reverse()
    t_set = t_set[:len(t)]
    t_set.sort()
    t_set.reverse()
    t_set = t_set[:K]
    result = 0
    for i in range(K):
        result += d[i]
    result += len(t_set) ** 2
    print(result)
