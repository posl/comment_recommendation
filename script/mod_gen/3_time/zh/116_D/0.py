def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi_dict = {}
    for i in range(n):
        if sushi[i][0] in sushi_dict.keys():
            sushi_dict[sushi[i][0]] += sushi[i][1]
        else:
            sushi_dict[sushi[i][0]] = sushi[i][1]
    sushi = []
    for key in sushi_dict.keys():
        sushi.append([key, sushi_dict[key]])
    sushi.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(k):
        ans += sushi[i][1]
    ans += k * k
    print(ans)
main()
