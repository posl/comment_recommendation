def main():
    n, w = map(int, input().split())
    cheese_list = []
    for _ in range(n):
        cheese_list.append(tuple(map(int, input().split())))
    cheese_list.sort(key=lambda x: x[0] / x[1], reverse=True)
    ans = 0
    for cheese in cheese_list:
        if w >= cheese[1]:
            ans += cheese[0]
            w -= cheese[1]
        else:
            ans += cheese[0] * w / cheese[1]
            break
    print(int(ans))
