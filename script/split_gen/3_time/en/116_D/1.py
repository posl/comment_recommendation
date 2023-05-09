def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        Sushi.append([t, d])
    Sushi.sort(key = lambda x: x[1], reverse = True)
    #print(Sushi)
    Sushi_t = [x[0] for x in Sushi]
    Sushi_d = [x[1] for x in Sushi]
    #print(Sushi_t)
    #print(Sushi_d)
    Sushi_t_unique = list(set(Sushi_t))
    #print(Sushi_t_unique)
    Sushi_t_unique.sort()
    #print(Sushi_t_unique)
    Sushi_t_unique_count = [0] * len(Sushi_t_unique)
    #print(Sushi_t_unique_count)
    for i in range(len(Sushi_t_unique)):
        Sushi_t_unique_count[i] = Sushi_t.count(Sushi_t_unique[i])
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
    if K >= len(Sushi_t_unique):
        print(sum(Sushi_d))
        return
    if K == 1:
        print(max(Sushi_d))
        return
    Sushi_t_unique_count = Sushi_t_unique_count[:K]
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count = Sushi_t_unique_count[1:]
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.append(K - len(Sushi_t_unique_count))
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count = Sushi_t_unique_count[:K]
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count = Sushi_t_unique_count[1:]
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.append(K - len(Sushi_t_unique_count))
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
