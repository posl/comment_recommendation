def main():
    N, K = map(int, input().split())
    sushi = [tuple(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    topping = set()
    topping.add(sushi[0][0])
    ans = sushi[0][1] + len(topping) ** 2
    left = 0
    right = 1
    while len(topping) < K and right < N:
        if sushi[right][0] not in topping:
            topping.add(sushi[right][0])
        right += 1
        while len(topping) > K:
            if sushi[left][0] in topping:
                topping.remove(sushi[left][0])
            left += 1
        ans = max(ans, sum(map(lambda x: x[1], sushi[left:right])) + len(topping) ** 2)
    print(ans)
