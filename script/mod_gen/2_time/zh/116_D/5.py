def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    t_count = [0] * n
    t_count_set = set()
    count = 0
    for i in range(k):
        count += sushi[i][1]
        if sushi[i][0] not in t_count_set:
            t_count_set.add(sushi[i][0])
            t_count[i] = 1
    result = count + len(t_count_set) ** 2
    for i in range(k, n):
        if t_count[i] != 0:
            continue
        for j in range(k - 1, -1, -1):
            if t_count[j] == 0:
                continue
            if sushi[i][0] in t_count_set:
                continue
            t_count_set.remove(sushi[j][0])
            t_count[j] = 0
            t_count_set.add(sushi[i][0])
            t_count[i] = 1
            count = count - sushi[j][1] + sushi[i][1]
            result = max(result, count + len(t_count_set) ** 2)
            break
    print(result)

if __name__ == '__main__':
    main()